from flask import Blueprint  , render_template
from flask_login import login_user , logout_user , login_required
from flask import Blueprint , render_template , request , redirect , url_for 
from models import User , Patient , Insurance , Procedure  , Tariff
from extension import db
from sqlalchemy import or_
from werkzeug.security import check_password_hash
import os
import shutil
from datetime import datetime
from flask import  flash , redirect , url_for 
from sqlalchemy.exc import IntegrityError

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
            username=username
        ).first()
        print(user)
        if user and check_password_hash(user.password , password):
            login_user(user)
            return redirect(url_for("main_up.dashboard"))

    return render_template("login.html")

#روت لاگین
@main_up.route("/")
def home():
    return render_template("login.html")

# روت لاگین
@main_up.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_up"))
# روت اضافه کردن بیمار
@main_up.route("/add-patient", methods=["GET", "POST"])
@login_required
def add_patient():
    if request.method == "POST":
        tariff = Tariff.query.filter_by(
            insurance_id = int(request.form["insurance_id"]),
            procedure_id = int(request.form["procedure_id"])).first()
        if tariff is None : 
            return "برای این بیمه و خدمت ثبت نشده است"
        exists = Patient.query.filter_by(
            national_code=request.form["national_code"]).first()
        if exists :
            return " بیماری قبلا با این کد ملی ثبت شده است"
        patient = Patient(
        full_name=request.form["full_name"],
        national_code=request.form["national_code"],
        phone=request.form["phone"],
        age=request.form["age"],
        gender=request.form["gender"],
        description=request.form["description"] ,
        insurance_id = request.form["insurance_id"],
        procedure_id = request.form["procedure_id"],
        total_price = tariff.price , paid_price = 0)
        try :
            db.session.add(patient)
            db.session.commit()
            flash ("بیمار با موفقیت ثبت شد")
            return redirect(url_for("main_up.add_patient"))
        except IntegrityError :
            db.session.rollback
            flash ("کد ملی قبلا ثبت شده است")
            

        
        print("pathient saved")
        return redirect(url_for("main_up.dashboard"))
    insurances = Insurance.query.all()
    procedures = Procedure.query.all()
    return render_template("add_patient.html" , insurances= insurances , procedures = procedures  )

 # روت داشبورد
@main_up.route("/dashboard") 
@login_required
def dashboard():
    search = request.args.get("search")
    print ("search" , search)
    if search :
        patients = Patient.query.filter(or_(
        Patient.full_name.contains(search) ,
        Patient.national_code.contains(search) ,
        Patient.phone.contains(search)
        )
        ).all()
    else:
        patients = Patient.query.all()
        patient_count= Patient.query.count()
        insurance_count = Patient.query.count()
        procedure_count = Patient.query.count()
        total_income = db.session.query(db.func.sum(Patient.total_price)).scalar() or 0
        received = db.session.query(db.func.sum(Patient.total_price)).scalar() or 0
        remaining = total_income - received
    return render_template("dashboard.html" , patients = patients , patient_count=patient_count ,insurance_count=insurance_count ,
         procedure_count=procedure_count , total_income=total_income ,received=received , remaining =remaining)
    

# روت حذف بیمار
@main_up.route("/delete-patient/<int:id>")
@login_required
def delete_patient(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect(url_for("main_up.dashboard"))

#روت ادیت اطلاعات بیمار
@main_up.route("/edit-patient/<int:id>" , methods=["GET" , "POST"])
@login_required
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

# روت بیمه
@main_up.route("/insurance" , methods=["GET" , "POST"])
@login_required
def insurance():
    if request.method == "POST":
        exists = Insurance.query.filter_by(
            name = request.form["name"]).first()
        if exists :
            return "این بیمه قبلا ثبت شده است"
        insurance = Insurance ( name = request.form["name"])
        db.session.add(insurance)
        db.session.commit()
        return redirect(url_for("main_up.insurance"))
    insurances = Insurance.query.order_by(Insurance.name).all()
    count = Insurance.query.count()
    return render_template("insurance.html" , insurances=insurances , count = count)

# روت پروسیجر
@main_up.route("/procedure" , methods = ["GET" , "POST"])
@login_required
def procedure():
    if request.method == "POST" :
        exists=  Procedure.query.filter_by(
            name = request.form["name"]).first()
        if exists :
            return "این خدمت قبلا ثبت شده است"
        procedures = Procedure(
            name=request.form["name"])
        db.session.add(procedures)
        db.session.commit()
        return  redirect(url_for("main_up.procedure"))
    procedures = Procedure.query.order_by(Procedure.name).all()
    count = Procedure.query.count()
    return render_template( "procedure.html" , procedures = procedures , count = count)

#حذف خدمت
@main_up.route("/delete-procedure/<int:id>")
@login_required
def  delete_procedure(id):
    procedure = Procedure.query.get_or_404(id) 
    db.session.delete(procedure)
    db.session.commit()
    return redirect(url_for("main_up.procedure"))

#ویرایش خدمت
@main_up.route("/edit-procedure/<int:id>", methods=["GET", "POST"])
@login_required
def edit_procedure(id):
    procedure = Procedure.query.get_or_404(id)
    if request.method == "POST":
        procedure.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("main_up.procedure"))

    return render_template("edit_procedure.html", procedure=procedure)


# روت تعرفه
@main_up.route("/tariff", methods=["GET", "POST"])
@login_required
def tariff():
    insurances = Insurance.query.all()
    procedures = Procedure.query.all()

    if request.method == "POST":
        tariff = Tariff(
            insurance_id=int(request.form["insurance_id"]),
            procedure_id=int(request.form["procedure_id"]),
            price=int(request.form["price"]))
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

# روت حذف تعرفه 
@main_up.route("/delete-tariff/<int:id>")
@login_required
def delete_tariff(id):
    tariff = Tariff.query.get_or_404(id) 
    db.session.delete(tariff)
    db.session.commit()
    return redirect(url_for("main_up.tariff"))

# روت ویرایش تعرفه
@main_up.route("/edit-tariff/<int:id>", methods=["GET", "POST"])
@login_required
def edit_tariff(id):
    tariff = Tariff.query.get_or_404(id)
    insurance = Insurance.query.all()
    procedure = Procedure.query.all()
    if request.method == "POST":
        tariff.insurance_id = int(request.form["insurance_id"])
        tariff.procedure_id = int(request.form["procedure_id"])
        tariff.price = int(request.form["price"])
        db.session.commit()
        return redirect(url_for("main_up.tariff"))

    return render_template("edit_tariff.html", procedure= procedure , insurance=insurance , tariff=tariff)



# روت تسویه
@main_up.route("/payment/<int:id>" , methods = ["GET" , "POST"])
@login_required
def payment(id):
    patient = Patient.query.get_or_404(id)
    if request.method == "POST" :
        amount = int(request.form["amount"])
        patient.paid_price += amount
        db.session.commit()
    return render_template("payment.html" , patient = patient)

# روت حذف بیمه بیمار
@main_up.route("/delete-insurance/<int:id>")
@login_required
def delete_insurance(id):
    insurance = Insurance.query.get_or_404(id) 
    db.session.delete(insurance)
    db.session.commit()
    return redirect(url_for("main_up.insurance"))

# روت ویرایش بیمه بیمار
@main_up.route("/edit-insurance/<int:id>", methods=["GET", "POST"])
@login_required
def edit_insurance(id):
    insurance = Insurance.query.get_or_404(id)

    if request.method == "POST":
        insurance.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("main_up.insurance"))

    return render_template("edit_insurance.html", insurance=insurance)
@main_up.route("/backup")
@login_required
def backup():
    source = os.path.join("instance" , "clinic,db")
    backup_folder = "backup"
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        filename = datetime.now().strftime("%y-%m-%d-%H-%M-%S.db")
        destination = os.path.join(backup_folder , filename)
        shutil.copy(source , destination)
        return "بکاپ با موفقیت گرفته شد"
