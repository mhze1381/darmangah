from extension import db 
class User(db.Model):
    id = db.Column( db.Integer , primary_key=True )
    username = db.Column(db.String(80) , unique=True , nullable=False )
    password = db.Column(db.String(255) , nullable = False)
class Insurance(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , unique=True , nullable=False)
 
class Procedure (db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , unique=True , nullable=False)

class Tariff(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    insurance_id = db.Column (db.Integer , db.ForeignKey("insurance.id") , nullable=False)
    procedure_id = db.Column (db.Integer , db.ForeignKey("procedure.id") , nullable=False )
    price = db.Column(db.Integer , nullable=False)
    insurance = db.relationship("Insurance")
    procedure = db.relationship("Procedure")


class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    national_code = db.Column(db.String(10), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    description = db.Column(db.Text)
    total_price = db.Column(db.Integer , default=0)
    paid_price = db.Column(db.Integer , default=0)
    insurance_id = db.Column (db.Integer , db.ForeignKey("insurance.id") , nullable=False )
    procedure_id = db.Column (db.Integer , db.ForeignKey("procedure.id") , nullable=False )
    insurance = db.relationship("Insurance")
    procedure = db.relationship("Procedure")
    insurance_id = insurance_id
    procedure_id = procedure_id
  

