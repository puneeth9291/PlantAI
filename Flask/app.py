from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from authlib.integrations.flask_client import OAuth
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

from .model import predict_image
from .utils import get_disease_info

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key-for-local-dev')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'Uploads')
app.config['FORUM_UPLOAD_FOLDER'] = os.path.join(app.config['UPLOAD_FOLDER'], 'forum_images')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Database configuration for deployment
default_db_uri = 'sqlite:///C:/Users/91967/db/users.db' if os.name == 'nt' else 'sqlite:///instance/users.db'
db_uri = os.getenv('DATABASE_URL', default_db_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Email configuration for password reset
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)

# Run migrations automatically on app startup
from flask_migrate import upgrade
with app.app_context():
    upgrade()

# OAuth setup for Google Sign-In
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

# Password reset serializer
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Association table for likes (many-to-many relationship)
post_likes = db.Table('post_likes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=True)  # Changed to String, nullable for Google users
    auth_provider = db.Column(db.String(20), default='local')  # 'local' or 'google'
    posts = db.relationship('Post', backref='user', lazy=True)
    liked_posts = db.relationship('Post', secondary=post_likes, backref=db.backref('liked_by', lazy='dynamic'))

# Post model for User Reviews
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.String(500))
    likes = db.Column(db.Integer, default=0)

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create database (initial creation, migrations handle updates)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
@login_required
def home():
    query_params = request.args.to_dict()
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('index.html', query_params=query_params, posts=posts)

@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    query_params = request.args.to_dict()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded', 'danger')
            return redirect(url_for('home', **query_params))
        file = request.files['file']
        if file.filename == '':
            flash('No file selected', 'danger')
            return redirect(url_for('home', **query_params))
        if not allowed_file(file.filename):
            flash('Invalid file type. Only PNG, JPG, JPEG, GIF allowed.', 'danger')
            return redirect(url_for('home', **query_params))

        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            with open(filepath, 'rb') as f:
                img_bytes = f.read()
            predicted_label = predict_image(img_bytes)
            info = get_disease_info(predicted_label)
        except Exception as e:
            flash(f'Error processing image: {str(e)}', 'danger')
            return redirect(url_for('home', **query_params))

        return render_template('display.html', filename=filename, **info, query_params=query_params)
    return render_template('index.html', query_params=query_params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    query_params = request.args.to_dict()
    if current_user.is_authenticated:
        return redirect(url_for('home', **query_params))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.auth_provider == 'google':
            flash("Please sign in using Google.", 'danger')
            return redirect(url_for('login', **query_params))
        if user and user.password and bcrypt.checkpw(password.encode('utf-8'), user.password):
            login_user(user)
            flash('Logged in successfully', 'success')
            return redirect(url_for('home', **query_params))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('login.html', query_params=query_params)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    query_params = request.args.to_dict()
    if current_user.is_authenticated:
        return redirect(url_for('home', **query_params))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if len(password) < 8 or not any(c.isdigit() for c in password) or not any(c in '!@#$%^&*()' for c in password):
            flash('Password must be at least 8 characters with 1 number and 1 special character', 'danger')
            return redirect(url_for('signup', **query_params))
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('signup', **query_params))

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('signup', **query_params))

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(name=name, email=email, password=hashed_password, auth_provider='local')
        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please log in.', 'success')
        return redirect(url_for('login', **query_params))
    return render_template('signup.html', query_params=query_params)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    query_params = request.args.to_dict()
    if current_user.is_authenticated:
        return redirect(url_for('home', **query_params))
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            token = serializer.dumps(email, salt='password-reset')
            reset_url = url_for('forgot_password', token=token, _external=True)
            msg = Message('PlantAI Password Reset', recipients=[email])
            msg.body = f'Click this link to reset your password: {reset_url}\nThis link will expire in 30 minutes.'
            try:
                mail.send(msg)
                flash('A password reset link has been sent to your email.', 'success')
            except Exception as e:
                print(f"Email error: {str(e)}")
                flash(f'Failed to send email: {str(e)}', 'danger')
        else:
            flash('Email not found', 'danger')
        return redirect(url_for('forgot_password', **query_params))
    token = request.args.get('token')
    if token:
        try:
            email = serializer.loads(token, salt='password-reset', max_age=1800)
            if request.method == 'POST':
                password = request.form['password']
                confirm_password = request.form['confirm_password']
                if password != confirm_password:
                    flash('Passwords do not match', 'danger')
                    return redirect(url_for('forgot_password', token=token, **query_params))
                if len(password) < 8 or not any(c.isdigit() for c in password) or not any(c in '!@#$%^&*()' for c in password):
                    flash('Password must be at least 8 characters long, contain a number, and a special character', 'danger')
                    return redirect(url_for('forgot_password', token=token, **query_params))
                user = User.query.filter_by(email=email).first()
                if user:
                    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                    user.password = hashed_password
                    db.session.commit()
                    flash('Password reset successfully! Please log in.', 'success')
                    return redirect(url_for('login', **query_params))
        except (SignatureExpired, BadSignature):
            flash('The reset link is invalid or has expired.', 'danger')
            return redirect(url_for('forgot_password', **query_params))
    return render_template('forgot-password.html', query_params=query_params)

@app.route('/auth/google')
def google_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    redirect_uri = url_for('google_callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/auth/google/callback')
def google_callback():
    try:
        token = google.authorize_access_token()
        user_info = token.get('userinfo')
        if not user_info:
            flash('Failed to retrieve user information', 'danger')
            return redirect(url_for('login'))

        email = user_info['email']
        name = user_info.get('name', email.split('@')[0])

        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(
                name=name,
                email=email,
                password=None,
                auth_provider='google'
            )
            db.session.add(user)
            db.session.commit()

        login_user(user)
        flash('Logged in successfully with Google', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        print(f"Google login error: {str(e)}")
        flash(f'Google login failed: {str(e)}', 'danger')
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    query_params = request.args.to_dict()
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('login', **query_params))

@app.route('/create_post', methods=['POST'])
@login_required
def create_post():
    query_params = request.args.to_dict()
    content = request.form['content']
    images = request.files.getlist('images')
    image_filenames = []

    if images and images[0].filename != '':
        os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'forum_images'), exist_ok=True)
        for image in images[:3]:
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'forum_images', filename)
            image.save(filepath)
            image_filenames.append(filename)

    new_post = Post(
        user_id=current_user.id,
        content=content,
        images=','.join(image_filenames) if image_filenames else None
    )
    db.session.add(new_post)
    db.session.commit()
    flash('Review posted successfully!', 'success')
    return redirect(url_for('home', **query_params) + '#community-forum')

@app.route('/like_post/<int:post_id>', methods=['POST'])
@login_required
def like_post(post_id):
    query_params = request.args.to_dict()
    post = Post.query.get_or_404(post_id)
    if current_user in post.liked_by:
        post.liked_by.remove(current_user)
        post.likes = max(0, post.likes - 1)
        flash('Like removed', 'success')
    else:
        post.liked_by.append(current_user)
        post.likes += 1
        flash('Post liked!', 'success')
    db.session.commit()
    return redirect(url_for('home', **query_params) + '#community-forum')

@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    query_params = request.args.to_dict()
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        flash('You can only delete your own posts', 'danger')
        return redirect(url_for('home', **query_params) + '#community-forum')
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('home', **query_params) + '#community-forum')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))