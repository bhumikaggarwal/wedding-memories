from flask import Flask, request

app = Flask(__name__)

events = [
    {"id": 1, "name": "Engagement"},
    {"id": 2, "name": "Haldi"},
    {"id": 3, "name": "Wedding"},
    {"id": 4, "name": "Reception"}
]


@app.get("/")
def home():
    return {"message": "Welcome to Wedding Memories Cloud"}


@app.get("/api/events")
def get_events():
    return events


@app.get("/api/events/<int:event_id>")
def get_event(event_id):
    for event in events:
        if event["id"] == event_id:
            return event

    return {"error": "Event not found"}, 404


@app.post("/api/events")
def create_event():
    data = request.get_json()

    new_event = {
        "id": len(events) + 1,
        "name": data["name"]
    }

    events.append(new_event)

    return new_event, 201


@app.put("/api/events/<int:event_id>")
def update_event(event_id):
    data = request.get_json()

    for event in events:
        if event["id"] == event_id:
            event["name"] = data["name"]
            return event, 200

    return {"error": "Event not found"}, 404


@app.delete("/api/events/<int:event_id>")
def delete_event(event_id):
    for event in events:
        if event["id"] == event_id:
            events.remove(event)
            return {"message": "Event deleted"}, 200

    return {"error": "Event not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)