from flask import Blueprint  , render_template
from flask_login import LoginManager
from flask import Blueprint , render_template , request , redirect , url_for 
from models import User , Patient
from extension import db
from sqlalchemy import or_

main_up = Blueprint("main_up" , __name__)
login_bp = Blueprint("login" , __name__)
@main_up.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username)
        print(password)

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()
        print(user)

        if user:
            return redirect(url_for("main_up.dashboard"))

    return render_template("login.html")



@main_up.route("/add-patient", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        patient = Patient(
            full_name=request.form["full_name"],
            national_code=request.form["national_code"],
            phone=request.form["phone"],
            age=request.form["age"],
            gender=request.form["gender"],
            description=request.form["description"] ,
            total_price = int(request.form["total_price"]),
            paid_price = int(request.form["paid_price"])
        )

        db.session.add(patient)
        db.session.commit()
        print("pathient saved")

        return redirect(url_for("main_up.dashboard"))

    return render_template("add_patient.html")



@main_up.route("/")
def home ():
    return render_template("login.html")

 
@main_up.route("/dashboard") 
def dashboard():
    search = request.args.get("search")
    if search :
        patients = Patient.query.filter(or_(
        Patient.full_name.contains(search) ,
        Patient.national_code.contains(search) ,
        Patient.phone.contains(search)
        )
        .all())
    else:
        
        patients = Patient.query.all()
        print("patients")
        return render_template("dashboard.html" , patients = patients)
    


@main_up.route("/delete-patient/<int:id>")
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for("main_up.dashboard"))
@main_up.route("/edit-patient/<int:id>" , methods=["GET" , "POST"])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)
    if request.method == "POST" :
        patient.full_name = request.form["full_name"]
        patient.national_code = request.form["national_code"]
        patient.phone = request.form["phone"]
        patient.age = request.form["age"]
        patient.gender = request.form["gender"]
        patient.description = request.form["description"]
        db.session.commit()
        print("update")
        return redirect(url_for("main_up.dashboard"))
    return render_template("edit_patient.html" , patient = patient)
