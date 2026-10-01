from models.events import Event


def get_events():
    return events

def get_event(event_id):
    for event in events:
        if event["id"] == event_id:
            return event

    return None

def create_event(data):
    new_event = {
        "id": len(events) + 1,
        "name": data["name"]
    }

    events.append(new_event)

    return new_event

def update_event(event_id, data):
    for event in events:
        if event["id"] == event_id:
            event["name"] = data["name"]
            return event
    return None

def delete_event(event_id):
    for event in events:
        if event["id"] == event_id:
            events.remove(event)
            return event
    return None