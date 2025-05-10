from markupsafe import Markup

disease_dic = {
    'Apple___Apple_scab': {
        'crop': 'Apple',
        'disease': 'Apple Scab',
        'cause': [
            "Apple scab overwinters primarily in fallen leaves and in the soil.",
            "Disease development is favored by wet, cool weather that generally occurs in spring and early summer.",
            "Fungal spores are carried by wind, rain, or splashing water from the ground to flowers, leaves, or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit."
        ],
        'prevention': [
            "Choose resistant varieties when possible.",
            "Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring.",
            "Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.",
            "Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores."
        ],
        'key_steps': [
            "Apply fungicides containing myclobutanil or sulfur during early spring.",
            "Prune trees to improve air circulation and reduce humidity around leaves.",
            "Apply dormant sprays like lime sulfur before bud break to kill overwintering spores.",
            "Monitor weather conditions to time fungicide applications during high-risk periods."
        ],
        'treatment': "Use copper-based fungicides applied every 7-10 days during spring to control the spread."
    },
    'Apple___Black_rot': {
        'crop': 'Apple',
        'disease': 'Black Rot',
        'cause': [
            "Black rot is caused by the fungus Diplodia seriata (syn Botryosphaeria obtusa).",
            "The fungus can infect dead tissue as well as living trunks, branches, leaves, and fruits.",
            "In wet weather, spores are released from these infections and spread by wind or splashing water. The fungus infects leaves and fruit through natural openings or minor wounds."
        ],
        'prevention': [
            "Prune out dead or diseased branches.",
            "Remove infected plant material from the area.",
            "Be sure to remove the stumps of any apple trees you cut down, as dead stumps can be a source of spores.",
            "Select disease-resistant cultivars when planting new trees."
        ],
        'key_steps': [
            "Remove all mummified fruits from the tree to reduce spore sources.",
            "Apply captan fungicide during bloom to protect new growth.",
            "Disinfect pruning tools regularly to prevent spreading the fungus.",
            "Destroy infected plant material by burning or deep burial."
        ],
        'treatment': "Combination of cultural controls (sanitation, pruning) and fungicide applications like captan or sulfur."
    },
    'Apple___Cedar_apple_rust': {
        'crop': 'Apple',
        'disease': 'Cedar Apple Rust',
        'cause': [
            "Fungal disease needing both apple and cedar trees to complete life cycle",
            "Spores form on junipers and travel to infect apple trees",
            "Reddish brown galls develop on cedar trees as source of spores"
        ],
        'prevention': [
            "Cut and remove galls from nearby juniper trees to limit spore spread.",
            "Plant apple trees far away from cedar or juniper trees whenever possible.",
            "Prune infected juniper branches at least 4–6 inches below the visible galls.",
            "Select and grow apple varieties that show resistance to cedar apple rust."
        ],
        'key_steps': [
            "Cut 4–6 inches below any visible galls on junipers",
            "Apply fungicides on apple trees during early spring",
            "Inspect regularly for signs of rust infection",
            "Manage surrounding junipers to reduce spore source"
        ],
        'treatment': "Apply protective fungicides like myclobutanil during early leaf and flower stages"
    },
    'Apple___healthy': {
        'crop': 'Apple',
        'disease': 'Healthy',
        'cause': ["No disease detected. Your crop is healthy!"],
        'prevention': ["Continue maintaining good cultural practices and regular crop monitoring."],
        'key_steps': ["Keep following a consistent care routine and monitor for any new symptoms."],
        'treatment': "No treatment needed."
    },

    'Blueberry___healthy': {
        'crop': 'Blueberry',
        'disease': 'Healthy',
        'cause': ["No disease detected. Your crop is healthy!"],
        'prevention': ["Maintain proper watering, pruning, and check regularly for early signs of issues."],
        'key_steps': ["Keep environment clean and plants well-spaced for good air circulation."],
        'treatment': "No treatment needed."
    },

    'Cherry_(including_sour)___Powdery_mildew': {
        'crop': 'Cherry',
        'disease': 'Powdery Mildew',
        'cause': [
            "Caused by Podosphaera clandestina fungus affecting young leaves, buds, and fruits.",
            "Overwinters as black bodies on dead leaves, tree crotches, and orchard floor."
        ],
        'prevention': [
            "Remove and destroy sucker shoots to limit the places where the fungus can grow.",
            "Use irrigation methods that keep the leaves dry and avoid wetting the fruits and foliage.",
            "Prune trees properly to improve air circulation and manage shoot growth with careful fertilization."
        ],
        'key_steps': [
            "Prune regularly to increase air circulation",
            "Use drip irrigation instead of overhead watering",
            "Apply sulfur-based or systemic fungicides during early growth stages",
            "Remove infected plant material promptly"
        ],
        'treatment': "Use fungicides like sulfur or myclobutanil at early signs of infection."
    },

    'Cherry_(including_sour)___healthy': {
        'crop': 'Cherry',
        'disease': 'Healthy',
        'cause': ["No disease detected. Your crop is healthy!"],
        'prevention': ["Ensure regular monitoring and proper orchard maintenance."],
        'key_steps': ["Practice good pruning and hygiene to keep trees healthy year-round."],
        'treatment': "No treatment needed."
    },

    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'crop': 'Corn (Maize)',
        'disease': 'Gray Leaf Spot',
        'cause': [
            "Gray leaf spot lesions reduce photosynthesis, affecting grain filling.",
            "Infection worsens when lesions spread past the ear leaves during pollination."
        ],
        'prevention': [
            "Focus on slowing the disease growth rate by protecting the leaf area until after grain formation.",
            "Rotate crops and use tillage practices that bury infected plant debris to reduce infection sources.",
            "Plant hybrids with resistance to gray leaf spot when possible to minimize risk."
        ],
        'key_steps': [
            "Scout fields early for signs of lesions",
            "Rotate crops to non-host species",
            "Apply fungicides if high disease pressure is present before tasseling",
            "Promote air flow through proper plant spacing"
        ],
        'treatment': "Apply fungicides like strobilurins or triazoles when early infection is detected."
    },

    'Corn_(maize)___Common_rust_': {
        'crop': 'Corn (Maize)',
        'disease': 'Common Rust',
        'cause': [
            "Caused by the fungus Puccinia sorghi, common in the U.S. cornfields.",
            "Infections are more severe with cool, wet weather, especially before silking."
        ],
        'prevention': [
            "Use highly resistant field corn hybrids to naturally minimize disease risk.",
            "Monitor popcorn and sweet corn more closely as they are more vulnerable to rust.",
            "Apply fungicides early if rust is detected before silking under cool and wet conditions."
        ],
        'key_steps': [
            "Scout early for rust symptoms especially on lower leaves",
            "Apply fungicides if heavy rust appears before silking",
            "Select resistant corn hybrids for planting",
            "Manage irrigation to avoid extended leaf wetness"
        ],
        'treatment': "Use fungicides like azoxystrobin or propiconazole if needed during early stages."
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
    'crop': 'Corn (Maize)',
    'disease': 'Northern Leaf Blight',
    'cause': [
        "Caused by the fungus Exserohilum turcicum (anamorph of Setosphaeria turcica).",
        "Characteristic cigar-shaped lesions; can cause significant yield loss in susceptible hybrids."
    ],
    'prevention': [
        "Use resistant corn hybrids where available.",
        "Adopt integrated management: crop rotation, proper field hygiene, and use of fungicides as needed.",
        "Scout fields regularly and monitor weather conditions conducive to disease spread."
    ],
    'key_steps': [
        "Apply fungicides preventatively when conditions favor disease development.",
        "Rotate corn with non-host crops to reduce pathogen survival.",
        "Remove and destroy infected plant debris after harvest."
    ],
    'treatment': "Fungicide applications based on hybrid susceptibility and local disease forecasts; prioritize products labeled for NCLB."
},

'Corn_(maize)___healthy': {
    'crop': 'Corn (Maize)',
    'disease': 'No Disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "Don't worry. Your crop is healthy. Keep it up!"
},

'Grape___Black_rot': {
    'crop': 'Grape',
    'disease': 'Black Rot',
    'cause': [
        "Fungus overwinters in canes, tendrils, and mummified berries.",
        "Spores are released during rain and infect young leaves and fruit stems.",
        "Infections visible after 8–25 days; continuous infection possible throughout spring and summer under wet conditions."
    ],
    'prevention': [
        "Space vines properly for good air circulation and sun exposure.",
        "Keep the area around vines free of weeds and tall grasses.",
        "Use protective fungicide sprays during key vine growth stages."
    ],
    'key_steps': [
        "First spray when shoots are 2–4 inches long, repeat at 10–15 inches, pre-bloom, post-bloom, and at fruit set.",
        "Remove mummified berries and infected debris during winter pruning.",
        "Choose resistant grape varieties if available."
    ],
    'treatment': "Use fungicides such as copper, captan, ferbam, mancozeb, or maneb according to label instructions."
},

'Grape___Esca_(Black_Measles)': {
    'crop': 'Grape',
    'disease': 'Black Measles (Esca)',
    'cause': [
        "Caused by a complex of fungi: mainly Phaeoacremonium spp. and Phaeomoniella chlamydospora.",
        "Spores are released during rainfall and infect pruning wounds."
    ],
    'prevention': [
        "Practice delayed and double pruning to minimize infection through fresh wounds.",
        "Apply pruning-wound protectants such as boric acid-based sealants or essential oils.",
        "Remove and destroy diseased wood and cankers during dry weather."
    ],
    'key_steps': [
        "Inspect vines in spring for dead spurs or stunted shoots.",
        "Surgically remove infected wood beyond visible cankers.",
        "Maintain good vineyard sanitation practices year-round."
    ],
    'treatment': "No direct chemical cure; preventative pruning-wound treatments are key."
},

'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
    'crop': 'Grape',
    'disease': 'Leaf Blight (Isariopsis Leaf Spot)',
    'cause': [
        "Fungus overwinters in fallen leaves and soil.",
        "Infection favored by wet, cool weather, typically in spring and early summer."
    ],
    'prevention': [
        "Choose resistant grape varieties if possible.",
        "Rake and destroy fallen leaves to reduce fungal spore load.",
        "Avoid overhead irrigation; water early in the day to allow foliage to dry."
    ],
    'key_steps': [
        "Maintain a clean vineyard floor to prevent splash dispersal of spores.",
        "Mulch with compost to block fungal spores in the soil.",
        "Scout frequently during periods of cool, damp weather."
    ],
    'treatment': "Use protective fungicides as needed, following recommended schedules during periods favorable for disease."
},

'Grape___healthy': {
    'crop': 'Grape',
    'disease': 'No Disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "Don't worry. Your crop is healthy. Keep it up!"
},

'Orange___Haunglongbing_(Citrus_greening)': {
    'crop': 'Orange',
    'disease': 'Citrus Greening (HLB)',
    'cause': [
        "Caused by bacteria Candidatus Liberibacter spp., affecting tree health, fruit development, and juice quality.",
        "Transmitted by the Asian Citrus Psyllid (ACP)."
    ],
    'prevention': [
        "Early detection and removal of symptomatic trees to prevent spread.",
        "Protect grove edges through intensive monitoring and pesticide use.",
        "Implement biological control programs targeting ACP vectors."
    ],
    'key_steps': [
        "Coordinate area-wide ACP management using Cooperative Huanglongbing Management Areas (CHMAs).",
        "Apply foliar nutritional sprays to maintain tree health, although these do not cure HLB.",
        "Regular grove inspection and immediate action when infection signs appear."
    ],
    'treatment': "Currently no cure; management focuses on vector control, early removal of infected trees, and maintaining tree health with nutritional support."
},
'Peach___Bacterial_spot': {
    'crop': 'Peach',
    'disease': 'Bacterial Spot',
    'cause': [
        "Caused by four species of Xanthomonas bacteria (X. euvesicatoria, X. gardneri, X. perforans, and X. vesicatoria)",
        "Bacteria are strictly aerobic, gram-negative rods with whip-like flagella for movement",
        "Spread occurs when bacteria move through water films on plant surfaces, invading wet tissues"
    ],
    'prevention': [
        "Always use pathogen-free certified seeds and thoroughly inspected disease-free transplants",
        "Avoid overwatering and reduce handling of seedlings when they are wet to minimize spread",
        "Sanitize trays, benches, tools, and greenhouse structures between seedling crops carefully",
        "Avoid working with plants when they are wet to reduce the risk of bacterial movement through wounds",
        "Implement strict greenhouse hygiene practices and maintain proper airflow to minimize leaf wetness"
    ],
    'key_steps': [
        "Monitor seedling crops closely and immediately remove and destroy any infected plants",
        "Apply copper-based bactericides early and at regular intervals during wet seasons",
        "Encourage vertical plant growth to improve air circulation and reduce leaf wetness duration",
        "Practice proper crop rotation and avoid replanting susceptible crops in previously infected areas"
    ],
    'treatment': "Spray copper-based bactericides weekly during periods of high humidity and rainfall; use streptomycin cautiously in early stages under expert guidance"
},

'Pepper,_bell___Bacterial_spot': {
    'crop': 'Pepper',
    'disease': 'Bacterial Spot',
    'cause': [
        "Caused by several gram-negative bacteria in the genus Xanthomonas",
        "Bacteria form yellow, mucoid colonies when cultured in laboratory conditions",
        "Bacterial masses ooze from leaf lesions, facilitating spread under wet conditions"
    ],
    'prevention': [
        "Use certified pathogen-free seeds and carefully inspect transplants before planting",
        "Rotate crops frequently and avoid planting peppers or tomatoes in the same location for at least two years",
        "Sanitize all tools, greenhouse surfaces, and containers before each planting cycle",
        "Limit irrigation to the root zone and avoid overhead watering to keep foliage dry",
        "Apply copper-based sprays proactively to protect healthy foliage and fruits from infection"
    ],
    'key_steps': [
        "Scout plants weekly for early signs of bacterial spot, especially after wet weather",
        "Use mulch or ground covers to prevent soil splashing onto leaves",
        "Enhance field drainage to prevent standing water that can promote bacterial spread",
        "Coordinate with local agricultural extension services for resistant cultivar recommendations and disease forecasting alerts"
    ],
    'treatment': "Regular copper-based bactericide applications, combined with mancozeb if copper resistance is suspected; remove severely infected plants to prevent spread"
},

'Peach___healthy': {
    'crop': 'Peach',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Continue good agricultural practices and regular monitoring to maintain crop health."
},

'Pepper,_bell___healthy': {
    'crop': 'Pepper',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Maintain strong crop hygiene, watering practices, and periodic health checks."
},
'Potato___healthy': {
    'crop': 'Potato',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Keep monitoring for early signs of disease and pests."
},

'Raspberry___healthy': {
    'crop': 'Raspberry',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Regular maintenance, pruning, and soil health checks are recommended."
},
'Soybean___healthy': {
    'crop': 'Soybean',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Maintain good crop management practices like timely irrigation, balanced fertilization, and regular scouting for pests."
},

'Strawberry___healthy': {
    'crop': 'Strawberry',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Keep monitoring for pests, maintain good mulching, and practice clean harvesting techniques."
},

'Tomato___healthy': {
    'crop': 'Tomato',
    'disease': 'No disease',
    'cause': [],
    'prevention': [],
    'key_steps': [],
    'treatment': "No treatment needed. Continue strong practices like pruning lower leaves, staking plants, and rotating crops annually."
},

'Potato___Early_blight': {
    'crop': 'Potato',
    'disease': 'Early Blight',
    'cause': [
        "Caused by the fungus Alternaria solani, common wherever potatoes are grown",
        "Primarily affects leaves and stems, leading to defoliation and potential tuber infection",
        "Primary infection can occur even without specific weather triggers, unlike late blight"
    ],
    'prevention': [
        "Use only disease-free, certified seed potatoes to minimize initial infection risk",
        "Implement a comprehensive foliar fungicide spray program throughout the growing season",
        "Kill vines properly before harvest to reduce tuber infections and disease carryover",
        "Allow tubers to fully mature before harvesting and only dig during dry conditions to minimize spread",
        "Handle potatoes gently during harvest and storage to prevent wounding that invites infection"
    ],
    'key_steps': [
        "Start fungicide treatments early, especially during warm, humid conditions favorable for the disease",
        "Practice a 3-4 year crop rotation, avoiding planting potatoes or tomatoes in the same soil consecutively",
        "Improve air circulation by providing proper plant spacing and using raised beds",
        "Inspect fields regularly for early signs such as dark, concentric leaf spots, and remove infected debris immediately"
    ],
    'treatment': "Use protectant fungicides like chlorothalonil or mancozeb, and systemic fungicides such as azoxystrobin, applied at 7-10 day intervals during high-risk periods."
},

'Potato___Late_blight': {
    'crop': 'Potato',
    'disease': 'Late Blight',
    'cause': [
        "Caused by the oomycete Phytophthora infestans, a water mold organism",
        "Multiple clonal lineages exist, some affecting both tomatoes and potatoes, others being host-specific",
        "Weeds like hairy nightshade can act as alternative hosts, contributing to disease spread"
    ],
    'prevention': [
        "Plant only healthy, thoroughly dried, and certified seed potatoes to avoid initial infections",
        "Inspect tomato and potato transplants carefully before planting, especially those from warmer southern regions",
        "Implement field sanitation by removing volunteer plants and controlling nightshade weeds",
        "Practice field rotation, avoiding solanaceous crops (like tomato and potato) for several years",
        "Monitor weather conditions closely, as cool, wet environments favor rapid disease spread"
    ],
    'key_steps': [
        "Apply preventive fungicide sprays starting before disease appearance, particularly under wet conditions",
        "Immediately remove, destroy, or deep-bury any infected plants at the first signs of late blight",
        "Use resistant potato and tomato varieties when available to minimize susceptibility",
        "Ensure good drainage in fields and use drip irrigation to keep foliage dry"
    ],
    'treatment': "Apply fungicides containing active ingredients like fluazinam, mandipropamid, or cymoxanil; initiate sprays preventively and repeat every 5-7 days during wet conditions; remove infected plants to stop spread."
},
'Squash___Powdery_mildew': {
    'crop': 'Squash',
    'disease': 'Powdery Mildew',
    'cause': [
        "Caused by fungal pathogens that thrive in humid conditions (68-81°F).",
        "Dry, warm environments help spores form and spread quickly by air.",
        "Older leaves show first symptoms mid to late summer, typically in areas like Minnesota.",
        "Spores are carried by the wind from infected leaves to healthy foliage.",
        "Under ideal conditions, the infection can rapidly cover the entire plant surface."
    ],
    'prevention': [
        "Apply fertilizer based on soil test results and avoid excess nitrogen that encourages lush, vulnerable growth.",
        "Ensure proper air circulation by spacing plants adequately, staking when necessary, and controlling weeds around the plants.",
        "Monitor plants weekly by examining multiple mature leaves across different field zones for early detection.",
        "Use resistant or tolerant squash varieties if available in regions with a history of powdery mildew issues."
    ],
    'key_steps': [
        "Remove severely infected leaves to reduce fungal spore load in the field.",
        "Water plants at the soil level, preferably in the morning, to keep leaves dry and limit fungal development.",
        "Implement crop rotation and avoid planting squash family crops (like cucumbers or pumpkins) consecutively in the same soil.",
        "Apply preventive fungicides, such as sulfur or potassium bicarbonate, especially during warm, humid periods."
    ],
    'treatment': "Use fungicides like sulfur, neem oil, potassium bicarbonate, or myclobutanil; start at the first signs of infection and repeat every 7–14 days based on weather and disease pressure."
},

'Strawberry___Leaf_scorch': {
    'crop': 'Strawberry',
    'disease': 'Leaf Scorch',
    'cause': [
        "Caused by the fungus Diplocarpon earliana, affecting mainly the foliage of strawberry plants.",
        "Early signs include small purplish spots on the topside of leaves, later enlarging and merging.",
        "Infected leaves eventually become scorched, dry, and curl upwards, reducing photosynthesis and plant vigor."
    ],
    'prevention': [
        "Remove all fallen infected leaves and plant debris from the strawberry patch during and after the growing season.",
        "Establish new strawberry transplants frequently to prevent buildup of fungal spores in old plantings.",
        "Plant strawberries in well-draining soil and avoid overwatering to limit fungal disease spread.",
        "Use resistant strawberry cultivars where available and avoid overhead irrigation that wets the foliage."
    ],
    'key_steps': [
        "Regularly monitor plants for early signs of purplish lesions and remove affected parts promptly.",
        "Avoid dense planting and ensure good air movement through proper plant spacing.",
        "Practice annual field sanitation, including removing weeds that may harbor fungal pathogens.",
        "Apply preventative fungicides like captan or myclobutanil if there is a known history of leaf scorch in the field."
    ],
    'treatment': "Apply fungicides such as captan, myclobutanil, or thiophanate-methyl according to label directions; start applications early in the season if conditions favor disease development."
},

'Tomato___Bacterial_spot': {
    'crop': 'Tomato',
    'disease': 'Bacterial Spot',
    'cause': [
        "Caused by four Xanthomonas species: X. euvesicatoria, X. gardneri, X. perforans, and X. vesicatoria.",
        "Bacteria are gram-negative rods, strictly aerobic, and move via a whip-like flagellum in water films on plant surfaces.",
        "Infection typically occurs during wet, humid weather, and bacteria enter through natural openings or wounds.",
        "Bacterial spot can affect leaves, stems, and fruits, reducing both plant vigor and marketable yield."
    ],
    'prevention': [
        "Use pathogen-free, certified seeds and disease-free transplants to prevent introducing the pathogen.",
        "Inspect all seedlings carefully before planting and reject any showing symptoms of bacterial spot.",
        "Avoid overhead watering and minimize plant handling when plants are wet to prevent bacteria spread.",
        "Regularly sanitize all tools, trays, benches, and greenhouse structures between seedling batches."
    ],
    'key_steps': [
        "Apply copper-based bactericides as a preventative measure, especially during wet or humid periods.",
        "Maintain proper plant spacing to promote airflow and quicker drying of foliage after rain or dew.",
        "Rotate crops with non-solanaceous plants (e.g., corn or beans) to break bacterial life cycles.",
        "Promptly remove and destroy heavily infected plants to limit disease spread within fields or greenhouses."
    ],
    'treatment': "Use copper-based bactericides (such as copper hydroxide or copper sulfate) mixed with mancozeb for enhanced effect; apply preventatively and at regular intervals during the growing season."
},
'Tomato___Early_blight': {
    'crop': 'Tomato',
    'disease': 'Early Blight',
    'cause': [
        "Caused by two closely related fungi: Alternaria tomatophila (more aggressive) and Alternaria solani.",
        "A. tomatophila is more common in some regions; where absent, A. solani takes over as the primary cause.",
        "Fungi infect leaves, stems, and fruits, leading to concentric ring patterns and plant defoliation."
    ],
    'prevention': [
        "Use pathogen-free seeds or save seeds only from disease-free plants.",
        "Practice crop rotation, avoiding tomatoes and related crops for at least two years.",
        "Control susceptible weeds like black nightshade and hairy nightshade, as well as volunteer tomatoes.",
        "Maintain proper soil nutrition, avoiding excessive potassium and ensuring sufficient nitrogen and phosphorus.",
        "Avoid working with wet plants after rain, irrigation, or dew to minimize fungal spread.",
        "Use drip irrigation to keep plant foliage dry."
    ],
    'key_steps': [
        "Monitor plants for early symptoms: target-shaped lesions on older leaves.",
        "Remove and destroy infected plant debris at season's end.",
        "Apply protective fungicides early in the season when conditions favor disease."
    ],
    'treatment': "Use fungicides containing chlorothalonil, mancozeb, or copper-based products; apply preventively and continue on a 7–10 day schedule during wet weather."
},

'Tomato___Late_blight': {
    'crop': 'Tomato',
    'disease': 'Late Blight',
    'cause': [
        "Caused by the water mold Phytophthora infestans, responsible for the historic Irish potato famine.",
        "Different clonal strains (e.g., US-23) can infect tomatoes, potatoes, and related species like hairy nightshade.",
        "Fungal spores spread rapidly under wet, cool conditions, leading to plant collapse if untreated."
    ],
    'prevention': [
        "Use certified disease-free seeds and transplants.",
        "Inspect transplants thoroughly for signs of late blight before planting.",
        "Avoid planting tomatoes near infected potato fields or nightshade weeds.",
        "Promote good air circulation with proper spacing and pruning to minimize humidity."
    ],
    'key_steps': [
        "Remove and destroy infected plants immediately if symptoms appear.",
        "Monitor plants daily during cool, wet periods (temperatures below 75°F, heavy dew).",
        "Implement drip irrigation to avoid wetting leaves.",
        "Apply fungicides as a preventive measure if late blight has been found nearby."
    ],
    'treatment': "Apply fungicides like chlorothalonil, mancozeb, or specific late blight fungicides (cyazofamid, fluopicolide); begin applications early and reapply based on label instructions during favorable conditions."
},

'Tomato___Leaf_Mold': {
    'crop': 'Tomato',
    'disease': 'Leaf Mold',
    'cause': [
        "Caused by the fungus Passalora fulva, which exclusively infects tomatoes.",
        "Begins with pale green to yellow spots on leaves, leading to brown moldy patches and withering.",
        "Fruit infections show as smooth black irregular areas at the stem end that become sunken and leathery."
    ],
    'prevention': [
        "Use drip irrigation instead of overhead watering to keep foliage dry.",
        "Space plants adequately and prune them to improve airflow.",
        "Sterilize stakes, ties, and tools with 10% bleach solution or commercial sanitizers between uses.",
        "Ensure good ventilation in greenhouses by using fans, vents, or by rolling up tunnel sides."
    ],
    'key_steps': [
        "Remove infected leaves as soon as they appear.",
        "Avoid dew formation by maintaining greenhouse night temperatures higher than outside.",
        "Destroy or bury crop residues away from tomato production areas at the end of the season."
    ],
    'treatment': "Apply fungicides containing chlorothalonil, mancozeb, or copper-based products early at the first signs of infection, and repeat applications as needed based on humidity and disease pressure."
},

'Tomato___Septoria_leaf_spot': {
    'crop': 'Tomato',
    'disease': 'Septoria Leaf Spot',
    'cause': [
        "Caused by the fungus Septoria lycopersici.",
        "Primarily attacks tomato foliage under prolonged wet, humid conditions, starting as small water-soaked spots with dark brown margins."
    ],
    'prevention': [
        "Remove and destroy infected leaves promptly when symptoms are noticed.",
        "Increase plant spacing to improve airflow and dry foliage quickly after rains.",
        "Apply mulch around plant bases to prevent soil splash, which spreads fungal spores.",
        "Avoid overhead irrigation that wets the foliage unnecessarily."
    ],
    'key_steps': [
        "Use fungicidal sprays preventively in wet and humid conditions.",
        "Maintain strict garden sanitation practices to limit fungal spread year after year.",
        "Rotate crops and avoid planting tomatoes in the same spot for at least two years."
    ],
    'treatment': "Use fungicidal sprays containing chlorothalonil, mancozeb, or copper compounds; start at early symptom detection and continue at regular intervals."
},
'Tomato___Spider_mites Two-spotted_spider_mite': {
    'crop': 'Tomato',
    'disease': 'Two-spotted Spider Mite',
    'cause': [
        "The two-spotted spider mite (Tetranychus urticae) is the most common mite attacking vegetables and fruits.",
        "Mites thrive under dry, dusty conditions and with excess nitrogen fertilization.",
        "Outbreaks are often triggered by early-season use of broad-spectrum insecticides that eliminate natural predators."
    ],
    'prevention': [
        "Avoid applying broad-spectrum insecticides early in the season.",
        "Do not over-fertilize plants, especially with nitrogen-rich fertilizers.",
        "Promote overhead irrigation or rely on natural rainfall to reduce mite populations."
    ],
    'key_steps': [
        "Monitor fields for early signs: stippling on leaves, webbing under leaves.",
        "Encourage natural predators like predatory mites or lady beetles.",
        "Apply miticides if population levels exceed economic thresholds."
    ],
    'treatment': "Use selective miticides targeting spider mites; rotate active ingredients to avoid resistance build-up."
},

'Tomato___Target_Spot': {
    'crop': 'Tomato',
    'disease': 'Target Spot',
    'cause': [
        "Fungal disease causing leaf loss and severe yield reduction if infection occurs before fruiting.",
        "Prevalent in screen houses and open fields, especially under humid tropical conditions."
    ],
    'prevention': [
        "Remove a few lower branches to improve airflow at the plant base.",
        "Remove and burn diseased lower leaves, particularly after harvesting lower fruit trusses.",
        "Weed regularly, as some weeds can serve as alternate hosts for the fungus.",
        "Avoid overhead irrigation to prevent ideal conditions for fungal spore production and spread."
    ],
    'key_steps': [
        "Inspect fields regularly for early leaf spotting symptoms.",
        "Prompt removal and destruction of infected material.",
        "Consider protective fungicide applications in highly susceptible areas."
    ],
    'treatment': "Use fungicides effective against fungal leaf spots, following label recommendations for timing and application intervals."
},

'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
    'crop': 'Tomato',
    'disease': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
    'cause': [
        "Transmitted persistently by whiteflies (Bemisia tabaci) in their adult stage.",
        "Virus acquisition is quick (15–20 minutes) and becomes transmissible after an 8–24 hour latent period."
    ],
    'prevention': [
        "Use insecticides to control whitefly populations, but rotate or mix products to prevent resistance.",
        "Plant resistant or tolerant tomato varieties where available.",
        "Implement crop rotation strategies to break whitefly and virus cycles."
    ],
    'key_steps': [
        "Scout fields regularly for whiteflies and symptoms of TYLCV (upward curling, yellowing leaves).",
        "Implement integrated pest management (IPM) programs to minimize whitefly populations.",
        "Develop and use transgenic tomatoes resistant to TYLCV for long-term control where available."
    ],
    'treatment': "No direct cure once infected; management focuses on whitefly control and planting resistant varieties."
},

'Tomato___Tomato_mosaic_virus': {
    'crop': 'Tomato',
    'disease': 'Tomato Mosaic Virus (ToMV)',
    'cause': [
        "Can persist for two years in dry soil or plant debris; survives shorter periods (one month) in moist soil.",
        "Spread primarily via human activity: contaminated hands, tools, clothing, and tobacco products (cigarettes).",
        "Seed transmission can occur but is less common compared to mechanical spread."
    ],
    'prevention': [
        "Purchase transplants only from reputable, sanitary sources.",
        "Inspect transplants carefully for any virus symptoms before planting.",
        "Avoid fields with old tomato root debris, which can harbor the virus for years.",
        "Maintain strict sanitation: wash hands thoroughly with soap and water before handling plants."
    ],
    'key_steps': [
        "Disinfect tools and equipment frequently during planting and maintenance activities.",
        "Train workers to recognize early virus symptoms and implement strict hygiene practices.",
        "Remove and destroy infected plants immediately to limit virus spread."
    ],
    'treatment': "No treatment exists; prevention through sanitation and resistant varieties is critical."
}
}

def get_disease_info(label):
    """Get structured disease information"""
    disease = disease_dic.get(label)
    
    if not disease:
        return {
            "error": "No information available for this disease"
        }
    
    # Convert lists to HTML-safe markup
    def format_list(items):
        return Markup('<br/>'.join(f'• {item}' for item in items))
    
    return {
        'crop': disease['crop'],
        'disease_name': disease['disease'],
        'cause': format_list(disease['cause']),
        'prevention': format_list(disease['prevention']),
        'key_steps': format_list(disease['key_steps']),
        'treatment': disease['treatment']
    }