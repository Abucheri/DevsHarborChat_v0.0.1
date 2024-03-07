import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .storage.database_storage import Base


class User(Base):
    """User class representing a chat user.

    Attributes:
        user_id (str): Unique identifier for the user.
        username (str): Username of the user.
        messages (list): List of messages associated with the user.
    """
    __tablename__ = 'users'

    user_id = Column(String(36), primary_key=True)
    username = Column(String(100))
    messages = relationship('Message', back_populates='user')

    def __init__(self, username):
        self.user_id = str(uuid.uuid4())
        self.username = username
