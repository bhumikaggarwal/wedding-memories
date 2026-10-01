from flask import Flask
from routes.event_routes import event_bp
from config.config import Config
from models import db
from models.events import Event


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()
app.register_blueprint(event_bp)


# @app.get("/")
# def home():
#     return {"message": "Welcome to Wedding Memories Cloud"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)