from flask import Flask, jsonify, send_file
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def login():
    return send_file("login.html")
@app.route("/home")
def home():
    return send_file("index.html")
@app.route("/report")
def report():
    return send_file("report.html")
# @app.route("/script.js")
# def script():
#    return send_file("script.js")
@app.route("/style.css")
def style():
   return send_file("style.css")


if __name__ == "__main__":
    app.run(port=5001, debug=True)

