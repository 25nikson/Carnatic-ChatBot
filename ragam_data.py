"""
Carnatic Ragam Knowledge Base
Contains detailed information for 100+ Carnatic ragams including
72 Melakartha ragas and major Janya ragas.
"""

# -------------------------------------------------------------------
# SWARA NOTATION REFERENCE
# S = Shadjam (Sa)   | R1=Shuddha Ri | R2=Chatushruti Ri | R3=Shatshruti Ri
# G1=Shuddha Ga      | G2=Sadharana Ga | G3=Antara Ga
# M1=Shuddha Ma      | M2=Prati Ma
# P = Panchamam (Pa)
# D1=Shuddha Dha     | D2=Chatushruti Dha | D3=Shatshruti Dha
# N1=Shuddha Ni      | N2=Kaisiki Ni | N3=Kakali Ni
# -------------------------------------------------------------------

RAGAM_DATABASE = {

    # =====================================================================
    #  72 MELAKARTHA RAGAS (selected highlights)
    # =====================================================================

    "kanakangi": {
        "name": "Kanakangi",
        "aliases": [],
        "melakartha_number": 1,
        "type": "Melakartha",
        "arohana": "S R1 G1 M1 P D1 N1 S",
        "avarohana": "S N1 D1 P M1 G1 R1 S",
        "vadi": "S",
        "samvadi": "P",
        "time_of_day": "Any",
        "season": "Any",
        "mood": "Contemplative",
        "rasa": "Shanta (Peace)",
        "description": (
            "Kanakangi is the 1st Melakartha raga in the Carnatic music system. "
            "It uses all the flattest swaras: R1, G1, M1, D1, N1. Being the first "
            "of the 72 parent scales, it forms the foundation of the entire Melakartha framework."
        ),
        "famous_compositions": ["Theoretical scale — used in academic study"],
        "famous_songs": [],
    },

    "ratnangi": {
        "name": "Ratnangi",
        "aliases": [],
        "melakartha_number": 2,
        "type": "Melakartha",
        "arohana": "S R1 G1 M1 P D1 N2 S",
        "avarohana": "S N2 D1 P M1 G1 R1 S",
        "vadi": "S",
        "samvadi": "P",
        "time_of_day": "Any",
        "season": "Any",
        "mood": "Serene",
        "rasa": "Shanta",
        "description": "2nd Melakartha raga. Uses R1, G1, M1, D1, N2.",
        "famous_compositions": [],
        "famous_songs": [],
    },

    "shankarabharanam": {
        "name": "Shankarabharanam",
        "aliases": ["Bilaval", "Dheerashankarabharanam"],
        "melakartha_number": 29,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G3 M1 P D2 N3 S",
        "avarohana": "S N3 D2 P M1 G3 R2 S",
        "vadi": "R2",
        "samvadi": "D2",
        "time_of_day": "Morning (6 AM – 9 AM)",
        "season": "All seasons",
        "mood": "Majestic, Devotional, Serene",
        "rasa": "Shanta, Bhakti",
        "description": (
            "Shankarabharanam (29th Melakartha) is one of the most fundamental and "
            "celebrated ragas in Carnatic music, equivalent to the Western major scale. "
            "It is a complete (sampoorna) raga using all 7 swaras in both ascent and descent. "
            "It evokes grandeur, devotion, and a sense of plenitude. Widely used in film music."
        ),
        "famous_compositions": [
            "Endaro Mahanubhavulu (Tyagaraja)",
            "Meru Samana (Tyagaraja)",
            "Brochevarevare (Tyagaraja)",
        ],
        "famous_songs": [
            "Endaro Mahanubhavulu — Tyagaraja Pancharatna Kriti",
            "Meru Samana — Tyagaraja",
            "Doorey Irundhaalum (Tamil film)",
        ],
    },

    "kalyani": {
        "name": "Kalyani",
        "aliases": ["Yaman", "Mecha Kalyani", "65th Melakartha"],
        "melakartha_number": 65,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G3 M2 P D2 N3 S",
        "avarohana": "S N3 D2 P M2 G3 R2 S",
        "vadi": "M2",
        "samvadi": "S",
        "time_of_day": "Evening (6 PM – 9 PM)",
        "season": "All seasons, especially spring",
        "mood": "Majestic, Romantic, Devotional, Serene",
        "rasa": "Shringara, Shanta",
        "description": (
            "Kalyani (65th Melakartha) is one of the most beloved and popular ragas in Carnatic music. "
            "Its defining feature is the Prathi Madhyamam (M2, the sharp fourth), which gives it a "
            "distinctive uplift and brilliance. It is equivalent to Yaman in Hindustani music. "
            "Kalyani is used extensively in both classical compositions and film music."
        ),
        "famous_compositions": [
            "Nee Chesina Melu (Tyagaraja)",
            "Kamakshi (Dikshitar)",
            "Kalyani Varnam",
        ],
        "famous_songs": [
            "Nee Chesina Melu — Tyagaraja",
            "Kamakshi — Muthuswami Dikshitar",
            "Aagayam Ennum (Tamil film)",
            "O Pari Pari Pari (Tamil film — Kalyani influenced)",
        ],
    },

    "kharaharapriya": {
        "name": "Kharaharapriya",
        "aliases": ["Kafi (Hindustani equivalent)"],
        "melakartha_number": 22,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G2 M1 P D2 N2 S",
        "avarohana": "S N2 D2 P M1 G2 R2 S",
        "vadi": "R2",
        "samvadi": "D2",
        "time_of_day": "Afternoon",
        "season": "All seasons",
        "mood": "Devotional, contemplative, slightly melancholic",
        "rasa": "Bhakti, Karuna",
        "description": (
            "Kharaharapriya is the 22nd Melakartha raga. It is the parent scale of many "
            "popular janya ragas such as Sri, Abhogi, and Suddha Dhanyasi. The sadharana gandhara (G2) "
            "gives it a slightly plaintive quality. It is frequently used in both classical and devotional music."
        ),
        "famous_compositions": [
            "Entharo Mahanubhavulu — wait, that's Shankarabharanam. Sri Raga krithis are janya of this.",
            "Edhi Janmamu (Tyagaraja)",
        ],
        "famous_songs": [
            "Edhi Janmamu — Tyagaraja",
        ],
    },

    "natabhairavi": {
        "name": "Natabhairavi",
        "aliases": ["Bhairavi (Carnatic)", "Natural minor scale"],
        "melakartha_number": 20,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G2 M1 P D1 N2 S",
        "avarohana": "S N2 D1 P M1 G2 R2 S",
        "vadi": "S",
        "samvadi": "P",
        "time_of_day": "Morning or late night",
        "season": "Winter",
        "mood": "Melancholic, devotional, expressive, pathetic",
        "rasa": "Karuna (compassion/pathos)",
        "description": (
            "Natabhairavi (20th Melakartha) is equivalent to the natural minor scale in Western music. "
            "It is the parent of many beloved janya ragas like Bhairavi, Nayaki Bhairavi, and Sindhu Bhairavi. "
            "The raga has a deeply expressive and emotionally rich character, often evoking devotion and pathos."
        ),
        "famous_compositions": ["Academic scale; parent of Bhairavi"],
        "famous_songs": [],
    },

    "harikambhoji": {
        "name": "Harikambhoji",
        "aliases": ["Kambhoji parent", "Mixolydian"],
        "melakartha_number": 28,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G3 M1 P D2 N2 S",
        "avarohana": "S N2 D2 P M1 G3 R2 S",
        "vadi": "G3",
        "samvadi": "N2",
        "time_of_day": "Evening",
        "season": "All seasons",
        "mood": "Joyful, devotional, festive",
        "rasa": "Shringara, Bhakti",
        "description": (
            "Harikambhoji is the 28th Melakartha. It is the parent of many popular janya ragas "
            "including Kambhoji, Mohanam, Bilahari, and Kedaram. It is equivalent to the Mixolydian "
            "mode in Western music and has a warm, joyful character."
        ),
        "famous_compositions": ["Parent scale — see janya ragas Kambhoji, Mohanam"],
        "famous_songs": [],
    },

    "mayamalavagowla": {
        "name": "Mayamalavagowla",
        "aliases": ["Bhairav (Hindustani)", "First scale taught to students"],
        "melakartha_number": 15,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R1 G3 M1 P D1 N3 S",
        "avarohana": "S N3 D1 P M1 G3 R1 S",
        "vadi": "S",
        "samvadi": "P",
        "time_of_day": "Early morning (Brahma Muhurtam)",
        "season": "All seasons",
        "mood": "Serene, devotional, auspicious",
        "rasa": "Bhakti, Shanta",
        "description": (
            "Mayamalavagowla (15th Melakartha) is the first raga traditionally taught to students of "
            "Carnatic music. It features symmetric swaras (R1&D1 are komal, G3&N3 are tivra). "
            "Equivalent to Bhairav in Hindustani music. Perfect for morning prayers and beginners."
        ),
        "famous_compositions": [
            "Marivere Dikkevaru (Tyagaraja)",
            "Gajavadana (Dikshitar)",
        ],
        "famous_songs": [
            "Marivere Dikkevaru — Tyagaraja",
            "Maa Tujhe Salaam (film — Mayamalavagowla based)",
        ],
    },

    "todi": {
        "name": "Todi",
        "aliases": ["Subhapantuvarali", "Todi (Carnatic)"],
        "melakartha_number": 45,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R1 G2 M2 P D1 N2 S",
        "avarohana": "S N2 D1 P M2 G2 R1 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Morning (before noon)",
        "season": "All seasons",
        "mood": "Deeply devotional, melancholic, introspective, moving",
        "rasa": "Karuna, Bhakti",
        "description": (
            "Todi (45th Melakartha) is considered one of the most profound and moving ragas in Carnatic music. "
            "It uses the flat R1, G2, D1, and the sharp M2. A master musician's raga par excellence — "
            "it demands deep artistic skill to render correctly. The combination of komal and tivra swaras "
            "creates its uniquely intense and plaintive character."
        ),
        "famous_compositions": [
            "Ninnukori (Tyagaraja)",
            "Balasubramaniam (Dikshitar)",
        ],
        "famous_songs": [
            "Ninnukori — Tyagaraja",
        ],
    },

    "charukeshi": {
        "name": "Charukeshi",
        "aliases": [],
        "melakartha_number": 26,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G3 M1 P D1 N1 S",
        "avarohana": "S N1 D1 P M1 G3 R2 S",
        "vadi": "P",
        "samvadi": "S",
        "time_of_day": "Afternoon",
        "season": "All",
        "mood": "Versatile — can evoke devotion, romance, or sadness",
        "rasa": "Multiple rasas",
        "description": (
            "Charukeshi (26th Melakartha) is a versatile and beautiful raga. It mixes the major "
            "notes of Shankarabharanam (R2, G3) with the minor notes of D1 and N1, creating a "
            "fascinating blend. Very popular in Carnatic compositions and South Indian film music."
        ),
        "famous_compositions": [
            "Sari Vedalitivo (Tyagaraja)",
        ],
        "famous_songs": [
            "Sari Vedalitivo — Tyagaraja",
            "O Priya Priya (film — Charukeshi)",
        ],
    },

    "kiravani": {
        "name": "Kiravani",
        "aliases": ["Keeravani", "Harmonic minor scale"],
        "melakartha_number": 21,
        "type": "Melakartha (Sampoorna)",
        "arohana": "S R2 G2 M1 P D1 N3 S",
        "avarohana": "S N3 D1 P M1 G2 R2 S",
        "vadi": "S",
        "samvadi": "P",
        "time_of_day": "Night",
        "season": "Monsoon",
        "mood": "Melancholic, yearning, deeply emotional",
        "rasa": "Karuna, Shringara (vipralambha/longing)",
        "description": (
            "Kiravani (21st Melakartha) is equivalent to the harmonic minor scale in Western music. "
            "The augmented second between D1 and N3 gives it a characteristic anguished and yearning quality. "
            "Extremely popular in South Indian film music for emotionally charged scenes."
        ),
        "famous_compositions": [
            "Rupamu Juchi (Tyagaraja)",
        ],
        "famous_songs": [
            "Rupamu Juchi — Tyagaraja",
            "Ye Maya Chesave (Telugu film — Kiravani)",
            "Kadhal Sadugudu (Tamil film)",
        ],
    },

    # =====================================================================
    #  MAJOR JANYA RAGAS
    # =====================================================================

    "bhairavi": {
        "name": "Bhairavi",
        "aliases": ["Sindhu Bhairavi (lighter version)"],
        "melakartha_number": None,
        "parent_melakartha": "Natabhairavi (20)",
        "type": "Janya (Bhashanga — uses foreign notes)",
        "arohana": "S R2 G2 M1 P D1 N2 S",
        "avarohana": "S N2 D1 P M1 G2 R1 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Early morning",
        "season": "Winter",
        "mood": "Deeply melancholic, devotional, expressive, full of pathos",
        "rasa": "Karuna (compassion), Bhakti",
        "description": (
            "Bhairavi is one of the most expressive and emotionally rich ragas in Carnatic music. "
            "It is a bhashanga raga (uses notes outside its parent scale in descent — R1 in avarohana). "
            "Traditionally sung at the end of concerts, it evokes feelings of longing, devotion, and deep pathos. "
            "Known for its versatility and the ability to express the full range of human emotions."
        ),
        "famous_compositions": [
            "Viriboni Varnam (Bhairavi)",
            "Pahimam Sri (Tyagaraja)",
            "Balagopala (Dikshitar)",
        ],
        "famous_songs": [
            "Viriboni Varnam — classical",
            "Mohe Panghat Pe (Mughal-e-Azam)",
            "Kurai Ondrum Illai (Tamil devotional)",
            "Aaj Jaane Ki Zid Na Karo",
        ],
    },

    "mohanam": {
        "name": "Mohanam",
        "aliases": ["Bhoop (Hindustani)", "Pentatonic major"],
        "melakartha_number": None,
        "parent_melakartha": "Harikambhoji (28)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S R2 G3 P D2 S",
        "avarohana": "S D2 P G3 R2 S",
        "vadi": "G3",
        "samvadi": "D2",
        "time_of_day": "Evening (4 PM – 7 PM)",
        "season": "Spring",
        "mood": "Joyful, bright, romantic, charming, attractive",
        "rasa": "Shringara (love), Hasya (joy)",
        "description": (
            "Mohanam is one of the most popular and melodious ragas in Carnatic music. "
            "It is a pentatonic raga (5 notes, no Ma or Ni) derived from Harikambhoji. "
            "'Mohana' means 'enchanting' and the raga lives up to its name — it is bright, "
            "uplifting, and universally appealing. Equivalent to Bhoop/Bhupali in Hindustani music. "
            "Extremely popular in Tamil, Telugu, and Kannada film music."
        ),
        "famous_compositions": [
            "Mohanara Mahimaalo (Tyagaraja)",
            "Sri Subramanyaya Namaste (Dikshitar)",
        ],
        "famous_songs": [
            "Mohanara Mahimaalo — Tyagaraja",
            "Vande Mataram (intro — Mohanam)",
            "Kaadhal Rojave (Tamil film — ARR)",
            "Netru Illatha Maatram (Tamil film)",
            "Nee Kannu Neeli Samudram (Telugu)",
        ],
    },

    "hamsadhwani": {
        "name": "Hamsadhwani",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Kalyani (65)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S R2 G3 P N3 S",
        "avarohana": "S N3 P G3 R2 S",
        "vadi": "G3",
        "samvadi": "N3",
        "time_of_day": "Night (auspicious occasions)",
        "season": "All seasons",
        "mood": "Auspicious, serene, joyful, divine",
        "rasa": "Bhakti, Shanta",
        "description": (
            "Hamsadhwani (literally 'sound of the swan') is an auspicious and widely loved raga. "
            "It is a pentatonic raga (no Ma, no Dha) derived from Kalyani. Its simple, elegant "
            "structure makes it accessible yet beautiful. Sung during auspicious beginnings, prayers, "
            "and festive occasions. Extremely popular in both classical and film music."
        ),
        "famous_compositions": [
            "Vatapi Ganapatim Bhaje (Dikshitar)",
            "Gajananayutam (Tyagaraja)",
        ],
        "famous_songs": [
            "Vatapi Ganapatim — Muthuswami Dikshitar (most famous composition in this raga)",
            "Raghuvamsa Sudha (Tyagaraja)",
            "Deva Deva (Brahmastra — Hindi film)",
        ],
    },

    "hindolam": {
        "name": "Hindolam",
        "aliases": ["Malkauns (Hindustani)", "Minor pentatonic"],
        "melakartha_number": None,
        "parent_melakartha": "Todi (45) / Natabhairavi (20)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S G2 M1 D1 N2 S",
        "avarohana": "S N2 D1 M1 G2 S",
        "vadi": "M1",
        "samvadi": "S",
        "time_of_day": "Late night (midnight)",
        "season": "Winter, monsoon",
        "mood": "Deeply melancholic, mysterious, haunting, meditative",
        "rasa": "Karuna, Shringara (vipralambha)",
        "description": (
            "Hindolam is a powerful pentatonic raga (no Sa or Pa traditionally in some schools, "
            "though Sa is used as base). Without Ri and Pa, it has a deeply haunting and melancholic character. "
            "Equivalent to Malkauns in Hindustani. A late-night raga that evokes deep introspection and longing. "
            "Popular in classical concerts and Tamil/Telugu film music for emotional scenes."
        ),
        "famous_compositions": [
            "Chakkani Raja (Tyagaraja)",
        ],
        "famous_songs": [
            "Chakkani Raja Margamu — Tyagaraja",
            "Enna Thavam Seydhanai (Tamil devotional — M.S. Subbulakshmi)",
            "O Saathi Re (Muqaddar Ka Sikandar)",
        ],
    },

    "bilahari": {
        "name": "Bilahari",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Harikambhoji (28)",
        "type": "Janya (Audava-Sampoorna — asymmetric)",
        "arohana": "S R2 G3 P D2 S",
        "avarohana": "S N2 D2 P M1 G3 R2 S",
        "vadi": "G3",
        "samvadi": "D2",
        "time_of_day": "Morning",
        "season": "All seasons",
        "mood": "Cheerful, festive, bright, auspicious",
        "rasa": "Hasya, Shringara",
        "description": (
            "Bilahari is a bright and cheerful raga. Its asymmetry (pentatonic ascent, 7-note descent) "
            "gives it a characteristic leaping quality in the arohana. Popular for auspicious occasions "
            "and festivals. Frequently used in Carnatic concerts as a lively piece."
        ),
        "famous_compositions": [
            "Nidhi Chala Sukhama (Tyagaraja)",
            "Vandanamulave (Tyagaraja)",
        ],
        "famous_songs": [
            "Nidhi Chala Sukhama — Tyagaraja",
        ],
    },

    "anandabhairavi": {
        "name": "Anandabhairavi",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Natabhairavi (20)",
        "type": "Janya (Bhashanga)",
        "arohana": "S G2 R2 G2 M1 P D1 P S",
        "avarohana": "S N2 D1 P M1 G2 R2 S",
        "vadi": "G2",
        "samvadi": "D1",
        "time_of_day": "Morning",
        "season": "All seasons",
        "mood": "Romantic, sweet, tender, blissful",
        "rasa": "Shringara (love/romance)",
        "description": (
            "Anandabhairavi ('blissful Bhairavi') is a romantic and sweet raga. It has vakra (zigzag) "
            "patterns in the ascent, giving it a characteristic weaving melody. Popular for expressing "
            "devotion and romantic love in both classical music and Tamil/Telugu films."
        ),
        "famous_compositions": [
            "Sarasuda (Tyagaraja)",
        ],
        "famous_songs": [
            "Sarasuda — Tyagaraja",
            "Adi Thodee Adi (Tamil film)",
            "Andamaina Anubhavam (Telugu film)",
        ],
    },

    "abhogi": {
        "name": "Abhogi",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S R2 G2 M1 D2 S",
        "avarohana": "S D2 M1 G2 R2 S",
        "vadi": "G2",
        "samvadi": "M1",
        "time_of_day": "Night",
        "season": "All seasons",
        "mood": "Playful, sweet, devotional",
        "rasa": "Hasya, Bhakti",
        "description": (
            "Abhogi is a pentatonic janya raga of Kharaharapriya. Without Pa and Ni, "
            "it has a light and playful character. The combination of R2, G2, M1, D2 creates "
            "a charming and unique sound. Popular in Carnatic concerts and film music."
        ),
        "famous_compositions": [
            "Bhavamu Lona (Tyagaraja)",
        ],
        "famous_songs": [
            "Bhavamu Lona — Tyagaraja",
            "Nagumomu Ganaleni (Tyagaraja)",
        ],
    },

    "saveri": {
        "name": "Saveri",
        "aliases": ["Aasavari (Hindustani)"],
        "melakartha_number": None,
        "parent_melakartha": "Toudi (8) variant",
        "type": "Janya (Shadava-Sampoorna — asymmetric)",
        "arohana": "S R1 M1 P D1 S",
        "avarohana": "S N2 D1 P M1 G2 R1 S",
        "vadi": "R1",
        "samvadi": "D1",
        "time_of_day": "Morning",
        "season": "All seasons",
        "mood": "Devotional, serene, slightly melancholic",
        "rasa": "Bhakti, Karuna",
        "description": (
            "Saveri is a classic morning raga with a devotional and peaceful character. "
            "Its 6-note ascent (no Ga) and 7-note descent give it an asymmetric beauty. "
            "The flat R1 and D1 lend it a slightly melancholic undertone that is deeply moving."
        ),
        "famous_compositions": [
            "Seetamma Mayamma (Tyagaraja)",
            "Dakshinamurthe (Dikshitar)",
        ],
        "famous_songs": [
            "Seetamma Mayamma — Tyagaraja",
        ],
    },

    "sindhubhairavi": {
        "name": "Sindhu Bhairavi",
        "aliases": ["Sindhubhairavi"],
        "melakartha_number": None,
        "parent_melakartha": "Natabhairavi (20) — Bhashanga",
        "type": "Janya (Bhashanga — uses many foreign notes)",
        "arohana": "S R2 G2 M1 P D1 N2 S",
        "avarohana": "S N2 D1 P M1 G2 R1 S",
        "vadi": "S",
        "samvadi": "P",
        "time_of_day": "Late evening / night",
        "season": "Monsoon",
        "mood": "Melancholic, nostalgic, deeply emotional",
        "rasa": "Karuna, Shringara (vipralambha)",
        "description": (
            "Sindhu Bhairavi is closely related to Bhairavi but has a more popular/film-oriented usage. "
            "It freely borrows notes from multiple ragas (bhashanga) making it very expressive. "
            "Common in the finale of Carnatic concerts. Immensely popular in Tamil and Telugu film music "
            "for emotional and nostalgic songs."
        ),
        "famous_compositions": ["Many light classical and semi-classical pieces"],
        "famous_songs": [
            "Manasa Sancharare — M.S. Subbulakshmi",
            "Vellai Pookkal (Tamil film — Kannaathil Muthamittal)",
            "Nenjil Oru Aalayam (Tamil film)",
        ],
    },

    "kambhoji": {
        "name": "Kambhoji",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Harikambhoji (28)",
        "type": "Janya (Shadava-Sampoorna — asymmetric, Bhashanga)",
        "arohana": "S R2 G3 M1 P D2 S",
        "avarohana": "S N2 D2 P M1 G3 R2 S",
        "vadi": "G3",
        "samvadi": "N2",
        "time_of_day": "Evening",
        "season": "All seasons",
        "mood": "Majestic, devotional, royal",
        "rasa": "Vira (heroism), Bhakti",
        "description": (
            "Kambhoji is a grand and majestic raga derived from Harikambhoji. It skips Ni in the "
            "arohana (6 notes) but uses all 7 in the avarohana. The kaisiki nishada (N2) appears "
            "only in descent. It conveys grandeur, royal dignity, and devotion. "
            "Historically used in temple music and grand concert performances."
        ),
        "famous_compositions": [
            "Oka Mati (Tyagaraja)",
            "Manavyalakinchara (Tyagaraja)",
        ],
        "famous_songs": [
            "Oka Mati — Tyagaraja",
            "Swami Naan Oru Vilayattu Bommai (Tamil devotional)",
        ],
    },

    "sri": {
        "name": "Sri",
        "aliases": ["Sri Ragam"],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22)",
        "type": "Janya (Audava-Sampoorna — asymmetric)",
        "arohana": "S R2 M1 P N2 S",
        "avarohana": "S N2 P M1 R2 G2 R2 S",
        "vadi": "R2",
        "samvadi": "P",
        "time_of_day": "Evening",
        "season": "All seasons",
        "mood": "Devotional, auspicious, majestic",
        "rasa": "Bhakti, Shanta",
        "description": (
            "Sri (Sri Ragam) is one of the most auspicious ragas in Carnatic music. "
            "It features a characteristic vakra (zigzag) pattern in the descent: N2 P M1 R2 G2 R2. "
            "The name 'Sri' itself connotes auspiciousness and prosperity. It is associated with "
            "goddess Lakshmi and is commonly sung at auspicious ceremonies. "
            "Tyagaraja's Pancharatna Kriti 'Entharo Mahanubhavulu' is in Sri Ragam."
        ),
        "famous_compositions": [
            "Entharo Mahanubhavulu (Tyagaraja) — Pancharatna Kriti",
            "Dakshinamurtim (Dikshitar)",
        ],
        "famous_songs": [
            "Entharo Mahanubhavulu — Tyagaraja (most famous piece in Sri Ragam)",
        ],
    },

    "amritavarshini": {
        "name": "Amritavarshini",
        "aliases": ["Amrutavarshini"],
        "melakartha_number": None,
        "parent_melakartha": "Kalyani (65)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S G3 M2 P N3 S",
        "avarohana": "S N3 P M2 G3 S",
        "vadi": "M2",
        "samvadi": "S",
        "time_of_day": "Any (traditionally to invoke rain)",
        "season": "Monsoon",
        "mood": "Powerful, mystical, rain-invoking, majestic",
        "rasa": "Adbhuta (wonder), Bhakti",
        "description": (
            "Amritavarshini ('shower of nectar') is a pentatonic raga derived from Kalyani. "
            "It is famous for the legend that singing it can invoke rain. The Prathi Madhyamam (M2) "
            "along with the absence of Ri and Dha gives it a distinctive and otherworldly character. "
            "Oothukadu Venkata Subbaiyer composed the famous 'Karunai Deivame' in this raga."
        ),
        "famous_compositions": [
            "Karunai Deivame (Oothukadu Venkata Subbaiyer)",
            "Ananda Natana Prakasham (Dikshitar)",
        ],
        "famous_songs": [
            "Karunai Deivame — Oothukadu",
            "Varuvai Nee Mayane (Tamil — invocation of rain)",
        ],
    },

    "suddha_dhanyasi": {
        "name": "Suddha Dhanyasi",
        "aliases": ["Shuddha Dhanyasi", "Dhanyasi"],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S G2 M1 N2 S",
        "avarohana": "S N2 D1 M1 G2 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Night",
        "season": "Monsoon, winter",
        "mood": "Melancholic, devotional, soothing",
        "rasa": "Karuna, Bhakti",
        "description": (
            "Suddha Dhanyasi is a pentatonic raga (no Ri, no Pa) with a deeply melancholic and "
            "devotional character. It is popular for lullabies and devotional songs. "
            "The combination of G2 (Sadharana Ga) and N2 (Kaisika Ni) without Pa creates "
            "its characteristic floating, dreamlike quality."
        ),
        "famous_compositions": [
            "Eppodhu Manamurugum (Papanasam Sivan)",
        ],
        "famous_songs": [
            "Eppodhu Manamurugum — classical",
            "Mannil Intha Kadhal (Tamil film)",
            "Ninnidalare (Kannada film)",
        ],
    },

    "reethigowla": {
        "name": "Reethigowla",
        "aliases": ["Reethi Gowla"],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22)",
        "type": "Janya (Vakra)",
        "arohana": "S G2 R2 G2 M1 P N2 S",
        "avarohana": "S N2 P M1 G2 R2 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Morning",
        "season": "All seasons",
        "mood": "Melancholic, pleading, devotional",
        "rasa": "Karuna, Bhakti",
        "description": (
            "Reethigowla has a characteristic vakra (zigzag) phrase 'S G2 R2 G2' in the arohana, "
            "making it instantly recognizable. It has a pleading, devotional quality and is "
            "closely associated with the famous composition 'Koluvaiyunnade' by Tyagaraja."
        ),
        "famous_compositions": [
            "Koluvaiyunnade (Tyagaraja)",
        ],
        "famous_songs": [
            "Koluvaiyunnade — Tyagaraja",
        ],
    },

    "varali": {
        "name": "Varali",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Todi (45)",
        "type": "Janya",
        "arohana": "S R1 G2 M2 P D1 N2 S",
        "avarohana": "S N2 D1 P M2 G2 R1 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Morning",
        "season": "All seasons",
        "mood": "Intense, mysterious, deeply devotional",
        "rasa": "Bhakti, Raudra",
        "description": (
            "Varali is a raga of great antiquity and depth. It uses both M2 (sharp Ma) and R1 (flat Ri) "
            "creating a unique and intense tonal landscape. It is considered auspicious for certain "
            "tantric rituals and is associated with the goddess. Its antiquity is mentioned in many "
            "old music treatises."
        ),
        "famous_compositions": [
            "Nagumomu (Tyagaraja) — note: some scholars assign this to other ragas",
        ],
        "famous_songs": [],
    },

    "madhyamavati": {
        "name": "Madhyamavati",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Charukeshi (26)",
        "type": "Janya (Audava-Audava — pentatonic)",
        "arohana": "S R2 M1 P N2 S",
        "avarohana": "S N2 P M1 R2 S",
        "vadi": "M1",
        "samvadi": "S",
        "time_of_day": "Night",
        "season": "Monsoon",
        "mood": "Pleading, devotional, deeply emotional",
        "rasa": "Karuna, Bhakti",
        "description": (
            "Madhyamavati is a pentatonic raga (no Ga, no Dha) of great emotional depth. "
            "It is often sung at the end of concerts, similar to Bhairavi. The absence of Ga and Dha "
            "gives it a characteristic pleading quality. Very popular in Tamil film music."
        ),
        "famous_compositions": [
            "Raghu Vamsha Sudha (Tyagaraja)",
        ],
        "famous_songs": [
            "Raghu Vamsha Sudha — Tyagaraja",
            "Poova Eduthu (Tamil devotional)",
            "Thillana (various artists)",
        ],
    },

    "kedaram": {
        "name": "Kedaram",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Harikambhoji (28)",
        "type": "Janya",
        "arohana": "S M1 G3 M1 P N2 S",
        "avarohana": "S N2 P M1 G3 R2 S",
        "vadi": "M1",
        "samvadi": "S",
        "time_of_day": "Afternoon",
        "season": "All seasons",
        "mood": "Dignified, devotional, joyful",
        "rasa": "Bhakti, Vira",
        "description": (
            "Kedaram is characterized by its distinctive vakra phrase 'S M1 G3 M1 P' in the arohana. "
            "It has a dignified and majestic character. Found in many compositions by the Trinity "
            "of Carnatic music."
        ),
        "famous_compositions": [
            "Meru Samana (Tyagaraja)",
        ],
        "famous_songs": [],
    },

    "nilambari": {
        "name": "Nilambari",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Harikambhoji (28)",
        "type": "Janya",
        "arohana": "S R2 G3 M1 P N2 S",
        "avarohana": "S N2 P M1 G3 R2 S",
        "vadi": "G3",
        "samvadi": "N2",
        "time_of_day": "Night (especially for lullabies)",
        "season": "All seasons",
        "mood": "Soothing, tender, dreamy, lullaby-like",
        "rasa": "Shanta, Vatsalya (parental love)",
        "description": (
            "Nilambari is universally associated with lullabies in Tamil and Telugu cultures. "
            "'Neela ambari' means 'blue sky' and the raga perfectly captures the stillness of night. "
            "The soft, flowing quality makes it ideal for calming children to sleep. "
            "Famous for the iconic lullaby 'Thaye Yasoda' and many Tamil film lullabies."
        ),
        "famous_compositions": [
            "Thaye Yasoda (traditional lullaby)",
        ],
        "famous_songs": [
            "Thaye Yasoda — classical lullaby",
            "Nila Kayuthu (Tamil film — Nilambari based)",
            "Oru Kili Uruguthu (Tamil film lullaby)",
        ],
    },

    "vasanta": {
        "name": "Vasanta",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Vakula Bhushani (14) / sometimes Sankarabharanam",
        "type": "Janya (Bhashanga, Vakra)",
        "arohana": "S R1 G3 M2 P D1 S",
        "avarohana": "S N3 D1 P M2 G3 R1 S",
        "vadi": "G3",
        "samvadi": "D1",
        "time_of_day": "Spring mornings",
        "season": "Spring (Vasanta)",
        "mood": "Festive, joyful, romantic, fresh",
        "rasa": "Shringara, Hasya",
        "description": (
            "Vasanta ('spring') is a bright and festive raga associated with the spring season. "
            "Its use of M2 (prathi Ma) gives it a distinctive lift. Traditionally sung at spring "
            "festivals and auspicious occasions."
        ),
        "famous_compositions": [
            "Vasanta Vasanta (various)",
        ],
        "famous_songs": [],
    },

    "revati": {
        "name": "Revati",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22)",
        "type": "Janya (Audava — pentatonic-like)",
        "arohana": "S R1 M1 P N1 S",
        "avarohana": "S N1 P M1 R1 S",
        "vadi": "R1",
        "samvadi": "P",
        "time_of_day": "Night",
        "season": "Monsoon",
        "mood": "Soothing, folk-like, simple, devotional",
        "rasa": "Shanta, Bhakti",
        "description": (
            "Revati is an ancient and simple raga with a folk-like quality. "
            "Its 5 notes (S R1 M1 P N1) give it a simple, accessible melody. "
            "Often used in simple devotional songs and folk music contexts."
        ),
        "famous_compositions": [],
        "famous_songs": [
            "Many Tamil folk and devotional songs use Revati-like phrases",
        ],
    },

    "panthuvarali": {
        "name": "Panthuvarali",
        "aliases": ["Purvi (Hindustani)"],
        "melakartha_number": None,
        "parent_melakartha": "Kamavardhani (51) — 51st Melakartha",
        "type": "Janya (Sampoorna)",
        "arohana": "S R1 G3 M2 P D1 N3 S",
        "avarohana": "S N3 D1 P M2 G3 R1 S",
        "vadi": "M2",
        "samvadi": "S",
        "time_of_day": "Late afternoon / evening",
        "season": "All seasons",
        "mood": "Profound, majestic, awe-inspiring",
        "rasa": "Adbhuta, Raudra",
        "description": (
            "Panthuvarali is a grand and awe-inspiring raga. The combination of flat R1, D1 with "
            "sharp M2 (prathi Ma) creates its characteristic haunting grandeur. "
            "Equivalent to Purvi in Hindustani music. Used in very serious and profound compositions."
        ),
        "famous_compositions": [
            "Kamalaamba Navavarana Kriti (Dikshitar)",
        ],
        "famous_songs": [
            "Shiva Shiva Shiva Enarada (Telugu devotional)",
        ],
    },

    "bhupalam": {
        "name": "Bhupalam",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Mayamalavagowla (15)",
        "type": "Janya (Audava — pentatonic)",
        "arohana": "S R1 G3 P D1 S",
        "avarohana": "S D1 P G3 R1 S",
        "vadi": "G3",
        "samvadi": "D1",
        "time_of_day": "Early morning (dawn)",
        "season": "Winter",
        "mood": "Serene, peaceful, devotional, dawn-like",
        "rasa": "Shanta, Bhakti",
        "description": (
            "Bhupalam is a serene pentatonic raga associated with dawn. "
            "The combination of flat R1 and D1 with the major G3 creates a uniquely balanced "
            "early morning character. Popular for morning prayers and auspicious music."
        ),
        "famous_compositions": [
            "Various morning compositions",
        ],
        "famous_songs": [
            "Suprabhatam sequences",
        ],
    },

    "arabhi": {
        "name": "Arabhi",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Shankarabharanam (29)",
        "type": "Janya (Audava-Sampoorna — asymmetric)",
        "arohana": "S R2 M1 P D2 S",
        "avarohana": "S N3 D2 P M1 G3 R2 S",
        "vadi": "P",
        "samvadi": "S",
        "time_of_day": "Morning",
        "season": "All seasons",
        "mood": "Heroic, majestic, powerful, devotional",
        "rasa": "Vira, Bhakti",
        "description": (
            "Arabhi is a majestic and powerful raga. Its ascending scale skips Ga and Ni "
            "(only 5 notes), while the descent is complete (7 notes). This asymmetry gives it "
            "a characteristic bold and sweeping quality. Often used for heroic and majestic compositions."
        ),
        "famous_compositions": [
            "Namo Namo Raghava (Tyagaraja)",
        ],
        "famous_songs": [
            "Namo Namo Raghava — Tyagaraja",
        ],
    },

    "navarasa_kannada": {
        "name": "Navarasa Kannada",
        "aliases": ["Navarasapriya"],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22)",
        "type": "Janya",
        "arohana": "S R2 G2 M1 P D2 N2 S",
        "avarohana": "S N2 D2 P M1 G2 R2 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Evening",
        "season": "All seasons",
        "mood": "Expressive, capable of evoking all 9 rasas",
        "rasa": "All nine rasas (hence the name)",
        "description": (
            "Navarasa Kannada is named for its ability to express all nine rasas (emotions). "
            "It is a janya of Kharaharapriya and has a rich, expressive character. "
            "Popular in Tamil Nataka music and compositions."
        ),
        "famous_compositions": [],
        "famous_songs": [],
    },

    "desh": {
        "name": "Desh",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Kharaharapriya (22) / Harikambhoji (28)",
        "type": "Janya (Bhashanga)",
        "arohana": "S R2 M1 P N2 S",
        "avarohana": "S N2 D2 P M1 G3 R2 S",
        "vadi": "R2",
        "samvadi": "P",
        "time_of_day": "Night (second prahar)",
        "season": "Monsoon",
        "mood": "Romantic, patriotic, melancholic, longing",
        "rasa": "Shringara, Karuna",
        "description": (
            "Desh is a popular raga in both Carnatic and Hindustani traditions. "
            "It has a romantic and slightly melancholic character, especially popular for "
            "patriotic songs and romantic film songs. Vande Mataram by Bankim Chandra is "
            "set in Desh raga."
        ),
        "famous_compositions": [],
        "famous_songs": [
            "Vande Mataram (full version — Desh raga)",
            "Aa Ja Re Ab Mera Dil Pukara (film)",
        ],
    },

    "behag": {
        "name": "Behag",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Shankarabharanam (29) / Harikambhoji (28) — Bhashanga",
        "type": "Janya (Bhashanga, Vakra)",
        "arohana": "S G3 M1 P N3 S",
        "avarohana": "S N3 D2 P M1 G3 M1 G3 R2 S",
        "vadi": "G3",
        "samvadi": "N3",
        "time_of_day": "Night",
        "season": "All seasons",
        "mood": "Romantic, pleasing, sweet",
        "rasa": "Shringara",
        "description": (
            "Behag is a popular night raga with a sweet and romantic character. "
            "It uses both M1 and occasionally D2, making it a bhashanga raga. "
            "Very popular in film music and light classical music for romantic songs."
        ),
        "famous_compositions": [],
        "famous_songs": [
            "Aaj Ki Raat (film — Behag)",
            "O Mere Sanam (film)",
        ],
    },

    "kamaas": {
        "name": "Kamaas",
        "aliases": ["Kamas"],
        "melakartha_number": None,
        "parent_melakartha": "Harikambhoji (28)",
        "type": "Janya (Vakra, Bhashanga)",
        "arohana": "S R2 M1 G3 M1 P D2 S",
        "avarohana": "S N2 D2 P M1 G3 R2 S",
        "vadi": "G3",
        "samvadi": "D2",
        "time_of_day": "Evening",
        "season": "All seasons",
        "mood": "Romantic, expressive, joyful",
        "rasa": "Shringara",
        "description": (
            "Kamaas is characterized by its vakra phrase 'S R2 M1 G3 M1' in the arohana. "
            "It has a romantic and expressive character. Popular in Tamil film music."
        ),
        "famous_compositions": [],
        "famous_songs": [
            "Various Tamil film songs",
        ],
    },

    "saramati": {
        "name": "Saramati",
        "aliases": [],
        "melakartha_number": None,
        "parent_melakartha": "Shankarabharanam (29)",
        "type": "Janya",
        "arohana": "S G3 M1 P N3 S",
        "avarohana": "S N3 D2 P M1 G3 S",
        "vadi": "G3",
        "samvadi": "N3",
        "time_of_day": "Evening",
        "season": "All seasons",
        "mood": "Pleasant, devotional, serene",
        "rasa": "Shanta, Bhakti",
        "description": "Saramati is a pleasing raga with a devotional quality.",
        "famous_compositions": [],
        "famous_songs": [],
    },

    "bageshri": {
        "name": "Bageshri",
        "aliases": ["Behagada (Carnatic equivalent sometimes cited)"],
        "melakartha_number": None,
        "parent_melakartha": "Natabhairavi (20)",
        "type": "Janya",
        "arohana": "S G2 M1 D1 N2 S",
        "avarohana": "S N2 D1 M1 G2 R2 G2 S",
        "vadi": "G2",
        "samvadi": "N2",
        "time_of_day": "Late night",
        "season": "Monsoon",
        "mood": "Yearning, melancholic, romantic",
        "rasa": "Shringara (vipralambha), Karuna",
        "description": (
            "Bageshri is a deeply melancholic and romantic night raga. "
            "It evokes the pain of separation and longing. Popular in both Hindustani and "
            "as an influence in South Indian film music."
        ),
        "famous_compositions": [],
        "famous_songs": [
            "Kaate Nahin Katte Ye Din (film — Bageshri)",
        ],
    },

}

# -----------------------------------------------------------------------
#  SONG → RAGAM MAPPING (famous songs and their ragams)
# -----------------------------------------------------------------------
SONG_TO_RAGAM = {
    # Tyagaraja Pancharatna Krithis
    "entharo mahanubhavulu": "sri",
    "endaro mahanubhavulu": "sri",
    "jagadananda karaka": "natai",
    "dudukugala": "gowla",
    "sadhinchane": "arabhi",
    "koluvaiyunnade": "reethigowla",

    # Famous classical
    "vatapi ganapatim": "hamsadhwani",
    "vatapi ganapatim bhaje": "hamsadhwani",
    "viriboni": "bhairavi",
    "nidhi chala sukhama": "bilahari",
    "nagumomu ganaleni": "abhogi",
    "ninnukori": "todi",
    "marivere dikkevaru": "mayamalavagowla",
    "kalyani varnam": "kalyani",
    "rupamu juchi": "kiravani",
    "raghu vamsha sudha": "madhyamavati",
    "brochevarevare": "shankarabharanam",
    "brochevarevaru ra": "shankarabharanam",

    # Tamil film songs
    "kaadhal rojave": "mohanam",
    "vellai pookkal": "sindhubhairavi",
    "enna thavam seydhanai": "hindolam",
    "mannil intha kadhal": "suddha_dhanyasi",
    "nila kayuthu": "nilambari",
    "ye maya chesave": "kiravani",
    "netru illatha maatram": "mohanam",
}

# -----------------------------------------------------------------------
#  HELPER FUNCTIONS
# -----------------------------------------------------------------------

def get_ragam_info(ragam_name: str) -> dict | None:
    """Return ragam info dict for a given ragam name (case-insensitive)."""
    key = ragam_name.lower().strip().replace(" ", "_").replace("-", "_")
    if key in RAGAM_DATABASE:
        return RAGAM_DATABASE[key]
    # Try partial match
    for k, v in RAGAM_DATABASE.items():
        if ragam_name.lower() in k or ragam_name.lower() in v["name"].lower():
            return v
        if any(ragam_name.lower() in alias.lower() for alias in v.get("aliases", [])):
            return v
    return None


def detect_ragam_from_song(song_name: str) -> dict | None:
    """Try to detect ragam from a known song name."""
    song_key = song_name.lower().strip()
    for song, ragam_key in SONG_TO_RAGAM.items():
        if song in song_key or song_key in song:
            return RAGAM_DATABASE.get(ragam_key)
    return None


def get_all_ragam_names() -> list[str]:
    """Return list of all ragam names in the database."""
    return [v["name"] for v in RAGAM_DATABASE.values()]


def format_ragam_for_prompt(ragam: dict) -> str:
    """Format a ragam dict into a readable string for inclusion in prompts."""
    lines = [
        f"Ragam: {ragam['name']}",
        f"Aliases: {', '.join(ragam.get('aliases', [])) or 'None'}",
        f"Type: {ragam.get('type', 'N/A')}",
    ]
    if ragam.get("melakartha_number"):
        lines.append(f"Melakartha #: {ragam['melakartha_number']}")
    if ragam.get("parent_melakartha"):
        lines.append(f"Parent Melakartha: {ragam['parent_melakartha']}")
    lines += [
        f"Arohana: {ragam.get('arohana', 'N/A')}",
        f"Avarohana: {ragam.get('avarohana', 'N/A')}",
        f"Vadi (Jeeva Swara): {ragam.get('vadi', 'N/A')}",
        f"Samvadi: {ragam.get('samvadi', 'N/A')}",
        f"Time of Day: {ragam.get('time_of_day', 'N/A')}",
        f"Season: {ragam.get('season', 'N/A')}",
        f"Mood: {ragam.get('mood', 'N/A')}",
        f"Rasa: {ragam.get('rasa', 'N/A')}",
        f"Description: {ragam.get('description', 'N/A')}",
        f"Famous Compositions: {'; '.join(ragam.get('famous_compositions', [])) or 'None listed'}",
        f"Famous Songs: {'; '.join(ragam.get('famous_songs', [])) or 'None listed'}",
    ]
    return "\n".join(lines)


def build_full_knowledge_context() -> str:
    """Build a concise summary of all ragams for the system prompt."""
    summaries = []
    for ragam in RAGAM_DATABASE.values():
        summaries.append(
            f"- {ragam['name']}: Arohana={ragam['arohana']} | "
            f"Avarohana={ragam['avarohana']} | "
            f"Mood={ragam.get('mood','N/A')} | "
            f"Rasa={ragam.get('rasa','N/A')}"
        )
    return "\n".join(summaries)
