import uuid
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from config import Config
from . import Base
from models.message import Message
from models.user import User


class DatabaseStorage:
    """
    DatabaseStorage class for storing chat users and messages in a database.

    Attributes:
        Session: SQLAlchemy session class.
        engine: SQLAlchemy engine.
    """

    def __init__(self, Session=None):
        if Session is not None:
            self.Session = Session
            self.engine = Session().bind
        else:
            engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
            Base.metadata.create_all(bind=engine)
            self.Session = sessionmaker(bind=engine)
            self.engine = engine

    def add_user(self, session, username):
        """
        Add a user to the database.

        Args:
            username (str): Username of the user.

        Returns:
            User: Created user object.
        """
        session = self.Session()
        user = User(username=username)
        session.add(user)
        session.commit()
        session.close()
        return user

    def get_users(self):
        """
        Retrieve all users from the database.

        Returns:
            list: List of dictionaries representing users.
        """
        session = self.Session()
        users = session.query(User).all()
        result = [{'user_id': user.user_id, 'username': user.username} for user in users]
        session.close()
        return result

    def add_message(self, user_id, username, content):
        """
        Add a message to the database.

        Args:
            user_id (str): User ID associated with the message.
            username (str): Username associated with the message.
            content (str): Content of the message.

        Returns:
            Message: Created message object.
        """
        session = self.Session()
        user = session.query(User).filter_by(user_id=user_id).first()
        message = Message(user_id=user_id, username=username, content=content)
        user.messages.append(message)
        session.commit()
        session.close()
        return message

    def get_messages(self):
        """
        Retrieve all messages from the database.

        Returns:
            list: List of dictionaries representing messages.
        """
        session = self.Session()
        messages = session.query(Message).all()
        result = [{'message_id': message.message_id, 'user_id': message.user_id,
                   'username': message.username, 'content': message.content}
                  for message in messages]
        session.close()
        return result