from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data=request.get_json()
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    title=data.get("title")

    print(title)
    events.append(Event(len(events)+1,title))
    return jsonify({
        "id" : len(events),
        "title": title 
    }), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data=request.get_json()
    if not data:
            return jsonify({"error": "JSON body required"}), 400
    title=data.get("title")
    if event_id <len(events):
        events[event_id].title=title
        return jsonify({
                "title": title 
        }), 200
    else:
        return jsonify({"error": "Invalid id"}) , 404    

@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = next(
        (event for event in events if event.id == event_id),
        None
    )

    if event is None:
        return jsonify({"error": "Invalid Id"}), 404

    events.remove(event)
    return "", 204
if __name__ == "__main__":
    app.run(debug=True)
