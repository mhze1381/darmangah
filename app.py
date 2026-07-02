from flask import Flask
from routes.routes import main_up
from config import Config
from extension  import db , login_manager
from models import User , Patient
from werkzeug.security import generate_password_hash , check_password_hash

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(main_up)
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username="darmangah").first():
        user = User(
            username="darmangah",
            password= generate_password_hash("12345678")
        ) 
        db.session.add(user)
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
  
if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)