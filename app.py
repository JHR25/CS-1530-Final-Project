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
    file = request.files['file']
    username = request.form['username']

    if file:
        data = json.load(file)
        manager.load_data(data)

        user_info = manager.get_user(username)
        if user_info:
            return render_template('sub_page.html', user=user_info)
        else:
            return "User not found"

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
