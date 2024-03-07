from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .database_storage import DatabaseStorage
from .file_storage import FileStorage