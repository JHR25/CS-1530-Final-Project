from flask import Flask, render_template, request, redirect
from SubscriptionManager import SubscriptionManager
import json

app = Flask(__name__)
manager = SubscriptionManager()

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['customer'] 

    try:
        with open('MockUserData.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        return "Mock data file not found"

    manager.load_data(data)
    user_info = manager.get_user(username)

    if user_info:
         return render_template('sub_page.html',
                               user_name=user_info.name,
                               subscriptions=[
                                   {
                                       'name': s.name,
                                       'type': s.type,
                                       'price': s.price,
                                       'usage': s.usage
                                   } for s in user_info.subscriptionList
                               ])
    else:
        return "User not found"

if __name__ == '__main__':
    app.run(debug=True)
