from flask import Flask , render_template
from extension import db
from config import Config
from routes import main_up

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(main_up)
with app.app_context():
        db.create_all
@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
        app.run(debug=True)