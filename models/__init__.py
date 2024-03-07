import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .storage.file_storage import FileStorage
from .storage.database_storage import DatabaseStorage
from config import Config

# Fetch credentials from environment variables
DB_USERNAME = os.environ.get('DB_USERNAME', 'your_username')
DB_DATABASE = os.environ.get('DB_DATABASE', 'your_database')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')

# Fetch storage type from environment variable
STORAGE_TYPE = os.environ.get('STORAGE_TYPE', 'database')

# Set default storage type to 'file' if not provided
if not STORAGE_TYPE:
    STORAGE_TYPE = 'file'

# Initialize the storage based on the chosen type
if STORAGE_TYPE == 'file':
    storage = FileStorage(file_path='messages.json')
elif STORAGE_TYPE == 'database':
    database_uri = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}'
    engine = create_engine(database_uri)
    Session = sessionmaker(bind=engine)
    storage = DatabaseStorage(Session)
else:
    raise ValueError(f"Invalid storage type: {STORAGE_TYPE}")