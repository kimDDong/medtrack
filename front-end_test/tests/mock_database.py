# mock_database.py

class MockDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users

    def clear(self):
        self.users = {}