import json

class SubscriptionManager:
    def __init__(self):
        self.data = {}

    def load_data(self, json_data):
        self.data = json_data

    def get_user(self, username):
        for user in self.data.get('user', []):
            if user.get('name') == username:
                return user
        return None
