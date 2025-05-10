<div align="center">

## 🌿 PLANT-AI [Enhanced Plant Disease Detection Web App]

### 🌐 <a href="https://your-deployment-link.com" target="_blank">Live Demo</a>

## <img src="./Assets/web.gif" alt="demo"/>

</div>

## 📌 Description

Food security for billions of people on earth requires minimizing crop damage through timely detection of diseases.  
This project provides a deep learning–based web application that can detect plant diseases using leaf image classification. It helps farmers and agronomists diagnose crop diseases more accurately and efficiently.

Originally created by [Soumyajit4419](https://github.com/soumyajit4419), this enhanced version features **improved frontend UI**, **responsive navigation**, and additional functionality.

---

## 🧪 Leaf Image Classification

## <img src="./Assets/batch.png" alt="batch of image"/>

This model detects diseases associated with plant leaves. Key steps:

### 1. Data Gathering

The dataset used is **"New Plant Diseases Dataset"**  
📥 Download: [Kaggle Dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset)  
It contains healthy and diseased crop leaf images.

### 2. Model Building

- Framework: **PyTorch**
- Models used:
  1. Custom CNN architecture
  2. Transfer Learning with **VGG16**
  3. Transfer Learning with **ResNet34**

### 3. Training

The best-performing model achieved **98.42% test accuracy** by tuning hyperparameters across the model variants.

### 4. Testing

Tested on **17,572 images** across **38 classes**.  
Example predictions:

<div>
  <img src="./Assets/out1.png" alt="index2" height="300px" width="450"/>
  <img src="./Assets/out2.png" alt="index3" height="300px"  width="450"/>
</div>

### 5. Model Accuracy and Configurations

<img src="./Assets/models.png" alt="models" />

---

## 🔍 Model Details

- 🔎 Detects **38 types of diseases**
- 🪴 Covers **14 unique plants**
- 📃 Detailed list of diseases and plants: See [`Src`](./Src)

---

## 🚀 Features of This Enhanced Version

- ✨ Improved user interface using HTML/CSS
- 📱 Responsive layout for mobile and desktop
- 🔒 Login, Signup, Forgot Password functionality
- ⚙️ Clean navigation and better UI/UX

---

## 🛠️ Tech Stack

- `Flask` – Backend Web Framework
- `PyTorch` – Deep Learning Model
- `HTML/CSS` – Frontend UI
- `Git LFS` – To handle large `.pth` model files

---

## 📂 Project Structure

- `Flask` : Code for server and deployment
- `TestImages` : Sample leaf images for testing
- `Src` : Source code for model training
- `Models` : Trained `.pth` models for prediction

---

## 📈 Future Work

- Implement **Image Localization** to detect infected regions
- Build a **Recommender System** for suitable pesticide suggestions
- Add **mobile app interface** for field usage

---

## 🧾 License

This project is licensed under the **MIT License**

---

## 🙏 Acknowledgements

This project is **based on** the work by [Soumyajit4419](https://github.com/soumyajit4419).  
🔧 This repository includes **significant frontend enhancements** and customizations by [Your Name](https://github.com/yourusername).

---

## 🌟 Show Your Support

Give a ⭐ to this repository if you find it useful!  
<!-- You can add your own donation button here -->
