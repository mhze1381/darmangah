from flask import Blueprint  , render_template
from flask_login import LoginManager
from flask import Blueprint , render_template , request , redirect , url_for 
from models import User
from 
main_up = Blueprint("main_up" , __name__)
login_bp = Blueprint("login" , __name__)
@main_up.route("/login" , methods = ["GET" , "POST "])
def login():
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username = username , password = password ).first()
        if user :
            return  redirect(url_for("main_up.dashborad"))
        
        return "seccessfull"
    return render_template("login.html")
@main_up.route("/")
def home ():
    return render_template("login.html")


