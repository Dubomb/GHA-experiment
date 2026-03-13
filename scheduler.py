from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

events = {}

@app.get("/events")
def get_events():
    return jsonify(events)

@app.get("/events/<string:event>")
def get_event(event):
    if event not in events:
        return {"error": "event with id not found"}, 404

    return events[event]

@app.post("/events")
def create_event():
    data = request.get_json()
    name = data.get("name", None)

    if name is None:
        return {"error": "name not found"}, 400
    
    id = str(uuid4())

    event = {
        "id": id,
        "name": name,
        "volunteers": []
    }

    events[id] = event

    return event