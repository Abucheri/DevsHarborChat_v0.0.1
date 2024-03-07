import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from models.user import User
from models import DatabaseStorage
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)

# Initialize the database storage
db_storage = DatabaseStorage()

# Use Flask-SQLAlchemy's session
session = db_storage.Session()


@app.route('/')
def index():
    """
    Render the index HTML template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')


@socketio.on('message')
def handle_message(msg):
    """
    Handle incoming chat messages.

    Args:
        msg (str): The received message.
    """
    print('Message:', msg)

    # Assume user information is available
    # (you'll implement user authentication later)
    user = db_storage.add_user(session, username="TestUser")

    # Store message using the chosen storage type
    message = db_storage.add_message(session, user_id=user.user_id,
                                     username=user.username, content=msg)

    socketio.emit('message', {
        'message_id': message.message_id,
        'user_id': user.user_id,
        'username': user.username,
        'message': msg
    })


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.close()


if __name__ == '__main__':
    socketio.run(app, debug=True)