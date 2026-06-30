from flask import Blueprint  , render_template
from flask_login import LoginManager
from flask import Blueprint , render_template , request , redirect , url_for 
from models import User

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

          
@main_up.route("/")
def home ():
    return render_template("login.html")
 
@main_up.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


