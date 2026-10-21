SYMPTOMS_DB = [
    {"id": "fever", "name": "Fever / Elevated Temp", "category": "General", "icon": "🌡️"},
    {"id": "fatigue", "name": "Fatigue / Weakness", "category": "General", "icon": "⚡"},
    {"id": "cough", "name": "Persistent Cough", "category": "Respiratory", "icon": "🫁"},
    {"id": "shortness_of_breath", "name": "Shortness of Breath", "category": "Respiratory", "icon": "😮‍💨"},
    {"id": "sore_throat", "name": "Sore Throat", "category": "Respiratory", "icon": "🗣️"},
    {"id": "headache", "name": "Severe Headache", "category": "Neurological", "icon": "🧠"},
    {"id": "chest_pain", "name": "Chest Pain / Pressure", "category": "Cardiovascular", "icon": "🫀"},
    {"id": "nausea", "name": "Nausea / Vomiting", "category": "Gastrointestinal", "icon": "🤢"},
    {"id": "loss_of_smell", "name": "Loss of Smell / Taste", "category": "Sensory", "icon": "👃"}
]

RULES_DB = [
    {
        "id": "R01",
        "condition": "Acute Respiratory Infection",
        "category": "Pulmonology",
        "required_symptoms": ["fever", "cough"],
        "verification_symptoms": ["shortness_of_breath", "sore_throat"],
        "guidance": "Rest, maintain adequate fluid intake, and monitor blood oxygen levels. Consult a practitioner if breathlessness develops.",
        "is_emergency": False
    },
    {
        "id": "R02",
        "condition": "Viral Prodrome Syndrome",
        "category": "General Medicine",
        "required_symptoms": ["fever", "fatigue"],
        "verification_symptoms": ["headache", "loss_of_smell"],
        "guidance": "Isolate, rest, and manage temperature with antipyretics under medical consultation.",
        "is_emergency": False
    },
    {
        "id": "R03",
        "condition": "Cardiac Crisis Alert",
        "category": "Cardiology",
        "required_symptoms": ["chest_pain"],
        "verification_symptoms": ["shortness_of_breath", "fatigue"],
        "guidance": "CRITICAL EMERGENCY: Immediate hospitalization and ECG assessment required!",
        "is_emergency": True
    }
]

RULES_DB = [
    {
        "id": "R01",
        "condition": "Acute Respiratory Infection",
        "category": "Pulmonology",
        "required_symptoms": ["cough"],
        "verification_symptoms": ["fever", "shortness_of_breath", "sore_throat"],
        "guidance": "Rest, maintain adequate fluid intake, and monitor blood oxygen levels. Consult a practitioner if breathlessness develops.",
        "is_emergency": False
    },
    {
        "id": "R02",
        "condition": "Viral / Sensorineural Infection",
        "category": "General Medicine",
        "required_symptoms": ["fever"],
        "verification_symptoms": ["fatigue", "headache", "loss_of_smell"],
        "guidance": "Isolate, rest, and manage temperature with antipyretics under medical consultation.",
        "is_emergency": False
    },
    {
        "id": "R03",
        "condition": "Upper Respiratory & Sensory Illness",
        "category": "ENT / Pulmonology",
        "required_symptoms": ["sore_throat"],
        "verification_symptoms": ["loss_of_smell", "shortness_of_breath", "cough"],
        "guidance": "Symptomatic relief, steam inhalation, and throat lozenges recommended.",
        "is_emergency": False
    },
    {
        "id": "R04",
        "condition": "Cardiac Crisis Alert",
        "category": "Cardiology",
        "required_symptoms": ["chest_pain"],
        "verification_symptoms": ["shortness_of_breath", "fatigue"],
        "guidance": "CRITICAL EMERGENCY: Immediate hospitalization and ECG assessment required!",
        "is_emergency": True
    }
]

SYMPTOMS_DB = [
    {"id": "fever", "name": "Fever / Elevated Temp", "category": "General", "icon": "🌡️"},
    {"id": "fatigue", "name": "Fatigue / Weakness", "category": "General", "icon": "⚡"},
    {"id": "cough", "name": "Persistent Cough", "category": "Respiratory", "icon": "🫁"},
    {"id": "shortness_of_breath", "name": "Shortness of Breath", "category": "Respiratory", "icon": "😮‍💨"},
    {"id": "sore_throat", "name": "Sore Throat", "category": "Respiratory", "icon": "🗣️"},
    {"id": "headache", "name": "Severe Headache", "category": "Neurological", "icon": "🧠"},
    {"id": "chest_pain", "name": "Chest Pain / Pressure", "category": "Cardiovascular", "icon": "🫀"},
    {"id": "nausea", "name": "Nausea / Vomiting", "category": "Gastrointestinal", "icon": "🤢"},
    {"id": "loss_of_smell", "name": "Loss of Smell / Taste", "category": "Sensory", "icon": "👃"}
]

RULES_DB = [
    {
        "id": "R01",
        "condition": "Acute Respiratory Infection",
        "category": "Pulmonology",
        "required_symptoms": ["cough"],
        "verification_symptoms": ["fever", "shortness_of_breath", "sore_throat"],
        "guidance": "Rest, maintain fluid intake, and monitor blood oxygen levels. Consult a doctor if breathlessness increases.",
        "is_emergency": False
    },
    {
        "id": "R02",
        "condition": "Viral Infection & Fatigue",
        "category": "General Medicine",
        "required_symptoms": ["fever"],
        "verification_symptoms": ["fatigue", "headache", "loss_of_smell"],
        "guidance": "Isolate, rest, and manage temperature with antipyretics under medical supervision.",
        "is_emergency": False
    },
    {
        "id": "R03",
        "condition": "Gastrointestinal Distress / Stomach Flu",
        "category": "Gastroenterology",
        "required_symptoms": ["nausea"],
        "verification_symptoms": ["fatigue", "fever", "headache"],
        "guidance": "Stay hydrated using Oral Rehydration Salts (ORS) and consume a light diet.",
        "is_emergency": False
    },
    {
        "id": "R04",
        "condition": "Neurological Migraine / Stress Headache",
        "category": "Neurology",
        "required_symptoms": ["headache"],
        "verification_symptoms": ["nausea", "fatigue"],
        "guidance": "Rest in a quiet, dark room and avoid bright light triggers.",
        "is_emergency": False
    },
    {
        "id": "R05",
        "condition": "Cardiac Emergency Warning",
        "category": "Cardiology",
        "required_symptoms": ["chest_pain"],
        "verification_symptoms": ["shortness_of_breath", "fatigue"],
        "guidance": "CRITICAL EMERGENCY: Seek immediate emergency hospitalization!",
        "is_emergency": True
    }
]