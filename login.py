from flask_login import LoginManager
from flask import Blueprint , render_template , request

login_bp = Blueprint("login" , __name__)
@login_bp.route("/login" , methods = ["GET" , "POST "])
def login():
    if request.method == "POST" :
        username = request.form.get("username")
        password = request.form.get("password")
        return "seccessfull"
    return render_template("login.html")