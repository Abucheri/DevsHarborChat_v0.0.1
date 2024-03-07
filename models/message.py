import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .storage import Base


class Message(Base):
    """
    Message class representing a chat message.

    Attributes:
        message_id (str): Unique identifier for the message.
        user_id (str): User ID associated with the message.
        username (str): Username associated with the message.
        content (str): Content of the message.
        user (User): User object associated with the message.
    """
    __tablename__ = 'messages'

    message_id = Column(String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey('users.user_id'))
    username = Column(String(100))
    content = Column(String(500))
    user = relationship('User', back_populates='messages')

    def __init__(self, user_id, username, content):
        self.message_id = str(uuid.uuid4())
        self.user_id = user_id
        self.username = username
        self.content = content