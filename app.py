from flask import Flask
from routes.routes import main_up
from config import Config
from extension  import db
from models import User , Patient



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(main_up)
with app.app_context():
    db.create_all()

    if not User.query.filter_by(username="darmangah").first():
        user = User(
            username="darmangah",
            password="12345678"
        )
        db.session.add(user)
        db.session.commit()
if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)