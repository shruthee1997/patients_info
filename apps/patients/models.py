from application.database import db


class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'dob': self.dob,
            'gender': self.gender,
            'mobile': self.mobile
        }

def get_all(id):
    if id:
        patient = Patients.query.get_or_404(id)
    else:
        patient = Patients.query.all()
    return patient

def insert(data):
    patient = Patients(name=data['name'], dob=data['dob'], gender=data['gender'], mobile=data['mobile'])
    db.session.add(patient)
    db.session.commit()
    return patient

def update(id, data):
    patient = Patients.query.get_or_404(id)
    if patient:
        patient.name = data.get('name', patient.name)
        patient.dob = data.get('dob', patient.dob)
        patient.gender = data.get('gender', patient.gender)
        patient.mobile = data.get('mobile', patient.mobile)
        db.session.commit()
        return patient

def delete(id):
    patient = Patients.query.get_or_404(id)
    if patient:
        db.session.delete(patient)
        db.session.commit()