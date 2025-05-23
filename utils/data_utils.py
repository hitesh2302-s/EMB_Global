import json

def load_patient_data(file_path="data/patients.json"):
    with open(file_path) as f:
        return json.load(f)
