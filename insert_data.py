import os
import json
from application import db, app

# Folder path containing the data files
folder_path = "update the data file path"

# with app.app_context():
#     db.create_all()

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        # Perform database insertion
        # Adjust the SQL query according to database schema
        for i in data["entry"]:
            if i["resource"]["resourceType"] == "Patient":
                with app.app_context():
                    from apps.patients.models import Patients
                    patient = Patients(name=i['resource']['name'][0]['given'][0], dob=i['resource']['birthDate'], gender=i['resource']['gender'], mobile=i['resource']['telecom'][0]['value'])
                    db.session.add(patient)
                    db.session.commit()
