from flask import Blueprint  , render_template
from flask_login import LoginManager
from flask import Blueprint , render_template , request , redirect , url_for 
from models import User , Patient
from extension import db

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
            description=request.form["description"]
        )

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for("main_up.dashboard"))

    return render_template("add_patient.html")
          
          
@main_up.route("/")
def home ():
    return render_template("login.html")
 
@main_up.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


