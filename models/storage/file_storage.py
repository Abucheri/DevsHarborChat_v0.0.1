import json

class FileStorage:
    """
    FileStorage class for storing chat messages in a JSON file.

    Attributes:
        file_path (str): Path to the JSON file.
        messages (list): List to store chat messages.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.messages = self.load_messages()

    def load_messages(self):
        """
        Load messages from the JSON file.

        Returns:
            list: List of stored messages.
        """

        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_message(self, message_data):
        """
        Save a message to the JSON file.

        Args:
            message_data (dict): Message data to be stored.
        """
        self.messages.append(message_data)
        with open(self.file_path, 'w') as file:
            json.dump(self.messages, file)