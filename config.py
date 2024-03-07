import os


class Config:
    """Configuration class for Flask application.

    Attributes:
            SECRET_KEY (str): Secret key for Flask application.
            SQLALCHEMY_DATABASE_URI (str): URI for connecting to the database.
    """
    # Generate a random secret key using os.urandom
    SECRET_KEY = os.urandom(24).hex()

    # Get database credentials from environment variables
    DB_USERNAME = os.environ.get('DB_USERNAME', 'your_username')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')
    DB_DATABASE = os.environ.get('DB_DATABASE', 'your_database')

    # Construct the database URI
    SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_DATABASE}'
