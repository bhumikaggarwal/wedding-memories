

from models import db

#
# events = [
#     {"id": 1, "name": "Engagement"},
#     {"id": 2, "name": "Haldi"},
#     {"id": 3, "name": "Wedding"},
#     {"id": 4, "name": "Reception"}
# ]




class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)