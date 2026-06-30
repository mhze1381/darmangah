from flask import Flask 
from extension import db
from config import Config
from routes import main_up
from models import User


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(main_up)
with app.app_context():
        db.create_all()
        if not User.query.filter_by(username ="admin").first():
                user =  User( username = "darmangeh" , password = "12345678")
        db.session.add(user)
        db.session.commit()
        app.run(debug=True)