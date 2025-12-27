from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Server online"

@app.route("/config")
def config():
    return jsonify({
        "server": "active",
        "version": "1.0",
        "message": "Connected successfully"
    })

if __name__ == "__main__":
    app.run()
