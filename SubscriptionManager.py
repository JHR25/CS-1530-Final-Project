import json
from dataclasses import dataclass
@dataclass
class Subscription: #a subscription class that is inside the user
    name: str
    type: str
    price: float
    usage: float
    def __str__(self):
        return f"{self.name} ({self.type}): ${self.price}/month; Used for {self.usage} hrs"
@dataclass
class User:
    name: str
    username:str
    password:str
    bank_account: str
    subscriptionList: list #list of subscriptions: not necessary safe?

class SubscriptionManager:
    def __init__(self):
        self.data = {} #data file
        self.users=[] #lsit of useres all with subscription lists

    def load_data(self, json_data):
        self.data = json_data
        self._createSubClasses()
    def _createSubClasses(self):# NEVER CALL THIS OUTSIDE OF LOAD DATA
        try:

            for user in self.data['user']:
                subs = [] #the user's subscription list
                for s in user['subscriptions']:
                    sub = Subscription(name=s['name'],type=s['type'],price=s['pricePerMonth'],usage=s['usageTimeHours'])
                    subs.append(sub)
                self.users.append(User(name=user['name'], username=user["username"],password=user["password"],bank_account=user['bank_account'], subscriptionList=subs))
        except:
            print("Something went wrong, make sure to run load_data() first")
    def get_user(self, username):
        for user in self.users:
            if user.name == username:
                return user.name
        return None
    def get_subscriptions(self,username):
        for user in self.users:
            if user.name == username:
                return user.subscriptionList
        return None
    def get_bank_account(self,username):
        for user in self.users:
            if user.name == username:
                return user.bank_account
        return None
    def get_username(self, username):
        for user in self.users:
            if user.name == username:
                return user.username
        return None
    def get_password(self, username):
        for user in self.users:
            if user.name == username:
                return user.password
        return None
    def print(self,username):
        subs=self.get_subscriptions(username)
        if subs==None:
            print("No User of this username found")
            return
        for i in subs:
            print(i)
