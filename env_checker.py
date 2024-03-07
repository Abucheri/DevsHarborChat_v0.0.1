import os

# Replace 'your_username', 'your_password', and 'your_database' with actual defaults if needed
DB_USERNAME = os.environ.get('DB_USERNAME', 'your_username')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'your_password')
DB_DATABASE = os.environ.get('DB_DATABASE', 'your_database')
STORAGE_TYPE = os.environ.get('STORAGE_TYPE', 'database')

print(f'DB_USERNAME: {DB_USERNAME}')
print(f'DB_PASSWORD: {DB_PASSWORD}')
print(f'DB_DATABASE: {DB_DATABASE}')
print(f'STORAGE_TYPE: {STORAGE_TYPE}')