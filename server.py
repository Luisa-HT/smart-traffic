from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cycle_data = {
    'greenTime': 0,
    "vehiclesDetected": 0
}
countdown = {
    "greenCount": 0
}
@app.route("/traffic-data")
def traffic_data():
    return jsonify(cycle_data)

@app.route("/countdown")
def countdown_data():
    return jsonify(countdown)

@app.route("/update-data/<int:green>/<int:vehicles>")
def update_data(green, vehicles):
    cycle_data["greenTime"] = green
    cycle_data["vehiclesDetected"] = vehicles
    return "Updated", 200

@app.route("/update-countdown/<int:count>")
def update_countdown(count):
    countdown["greenCount"] = count
    return "Updated", 100

if __name__ == "__main__":
    app.run(port=5000, debug=True)