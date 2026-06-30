from extension import db 
class User(db.Model):
    id = db.Column( db.Integer , primary_key=True )
    username = db.Column(db.String(80) , unique=True , nullable=False )
    password = db.Column(db.String(255) , nullable = False)

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

