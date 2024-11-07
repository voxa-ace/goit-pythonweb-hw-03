from flask import Flask, render_template_string, request, jsonify, send_from_directory, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__)

DATA_FILE = "storage/data.json"
os.makedirs("storage", exist_ok=True)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

@app.route('/')
def index():
    with open("index.html") as f:
        return f.read()

@app.route('/message.html')
def message():
    with open("message.html") as f:
        return f.read()

@app.route('/read.html')
def read():
    with open("read.html") as f:
        return f.read()

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.form
    username = data.get("username")
    message = data.get("message")
    if username and message:
        with open(DATA_FILE, "r+") as f:
            content = json.load(f)
            content[str(datetime.now())] = {"username": username, "message": message}
            f.seek(0)
            json.dump(content, f, indent=4)
    return redirect(url_for('index'))

@app.route('/get_messages')
def get_messages():
    with open(DATA_FILE) as f:
        messages = json.load(f)
    return jsonify(messages)

@app.route('/<filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.errorhandler(404)
def page_not_found(e):
    with open("error.html") as f:
        return f.read(), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
