from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin='*')

message_storage = []

@socketio.on('connect')
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Disconnected')

@socketio.on('message')
def handle_message(message):
    print(f"Message: {message}")
    message_storage.append(message)
    socketio.emit('message', message)

for msg in message_storage:
    print(f"Stored Message: {msg}")

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)