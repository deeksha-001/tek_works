def find_by_disease(patients, disease):
    return [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]

patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

search_disease = "Flu"
print("Patients with", search_disease + ":", find_by_disease(patients, search_disease))
