from flask import Blueprint  , render_template
from flask_login import LoginManager
from flask import Blueprint , render_template , request , redirect , url_for 
from models import User , Patient , Insurance , Procedure  , Tariff
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
        tariff = Tariff.query.filter_by(
            insurance_id = int(request.form["insurance_id"]),
            procedure_id = int(request.form["procedure_id"]).first() 
        if tariff is None 
            return "برای این بیمه و خدمت ثبت نشده است"
        )
        patient = Patient(
            full_name=request.form["full_name"],
            national_code=request.form["national_code"],
            phone=request.form["phone"],
            age=request.form["age"],
            gender=request.form["gender"],
            description=request.form["description"] ,
            insurance_id = request.form["insurance_id"],
            procedure_id = request.form["procedure_id"], 
            total_price = int(request.form["total_price"]),
            paid_price = int(request.form["paid_price"]),
            total_price = tariff.price , paid_price = 0
        )

        db.session.add(patient)
        db.session.commit()
        print("pathient saved")

        return redirect(url_for("main_up.dashboard"))
    insurances = Insurance.query.all()
    procedures = Procedure.query.all()
    return render_template("add_patient.html" , insurance= insurances , procedures = procedures  )



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
        ).all()
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

@main_up.route("/insurance" , methods=["GET" , "POST"])
def insurance():
    if request.method == "POST":
        insurance = Insurance ( name = request.form["name"])
        db.session.add(insurance)
        db.session.commit()
        return redirect(url_for("main_up.insurance"))
    insurances = Insurance.query.all()
    return render_template("insurence.html" , insurances=insurances)

@main_up.route("/procedure" , methods = ["GET" , "POST"])
def procedure():
    if request.method == "POST" :
        procedures = Procedure(
            name=request.form["name"]
        )
        db.session.add(procedure)
        db.session.commit()
        return  redirect(url_for(main_up.procedure))
    return render_template( "procedure.html" , procedures = procedures)
@main_up.route("/tariff", methods=["GET", "POST"])
def tariff():
    insurances = Insurance.query.all()
    procedures = Procedure.query.all()

    if request.method == "POST":
        tariff = Tariff(
            insurance_id=int(request.form["insurance_id"]),
            procedure_id=int(request.form["procedure_id"]),
            price=int(request.form["price"])
        )

        db.session.add(tariff)
        db.session.commit()
        return redirect(url_for("main_up.tariff"))

    tariffs = Tariff.query.all()

    return render_template(
        "tariff.html",
        insurances=insurances,
        procedures=procedures,
        tariffs=tariffs
    )
