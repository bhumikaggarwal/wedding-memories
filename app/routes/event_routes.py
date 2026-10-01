from flask import Blueprint,request
from services.event_service import get_events,get_event,create_event,update_event,delete_event

event_bp = Blueprint('event', __name__)

@event_bp.get("/api/events")
def get_all_events():
    return get_events()

@event_bp.get("/api/events/<int:event_id>")
def get_single_event(event_id):
    event = get_event(event_id)
    if event is None:
        return {"error": "Event not found"}, 404

    return event

@event_bp.post("/api/events")
def create_single_event():
    data = request.get_json(silent=True)
    if data is None:
        return {"error" : "Request must contain valid JSON data"}, 400
    if "name" not in data:
        return {"error" : "Name field is required"}, 400
    if not isinstance(data["name"], str):
        return {"error" : "Name field must be a string"}, 400
    if data["name"].strip() == "":
        return {"error" : "Name field cannot be empty"}, 400
    return create_event(data),201

@event_bp.put("/api/events/<int:event_id>")
def update_single_event(event_id):
    data = request.get_json(silent=True)
    if data is None:
        return {"error" : "Request must contain valid JSON data"}, 400
    if "name" not in data:
        return {"error" : "Name field is required"}, 400
    if not isinstance(data["name"], str):
        return {"error" : "Name field must be a string"}, 400
    if data["name"].strip() == "":
        return {"error" : "Name field cannot be empty"}, 400
    return update_event(event_id, data),200

@event_bp.delete("/api/events/<int:event_id>")
def delete_single_event(event_id):
    event = delete_event(event_id)
    if event is None:
        return {"error": "Event not found"}, 404

    return {"message": "Event deleted"}, 200
