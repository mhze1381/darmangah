from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
with app.app_context():
    db.create_all()

    if not User.query.filter_by(username="darmangeh").first():
        user = User(
            username="darmangeh",
            password="12345678"
        )
        db.session.add(user)
        db.session.commit()
