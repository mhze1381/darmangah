from extension import db 
class User(db.Model):
    id = db.Column( db.Integer , primary_key=True )
    username = db.Column(db.String(80) , unique=True , nullable=False )
    password = db.Column(db.String(255) , nullable = False)
class Insurance(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , unique=True , nullable=False)
 
class Proceduree (db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(100) , unique=True , nullable=False)

    class Tariff(db.Model):
       id = db.Column(db.Integer , primary_key=True)
       Insurance_id = db.Column (db.Integer , db.Foreignkey("insurance_id") , nullable=False)
       price = db.Column(db.Integer , nullable=False)



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
    insurance_id = db.Column (db.Integer , db.ForeignKey("insurance_id") , nullable=False )
    procedure_id = db.Column (db.Integer , db.ForeignKey("procedure_id") , nullable=False )
    insurance = db.relationship("Incurance")
    procedure = db.relationship("Procedure")
    paid_price = db.Column(db.Integer , default=0)

