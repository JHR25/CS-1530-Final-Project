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
    if "customer" in request.form:
        global username
        username = request.form['customer']
        bank_number = request.form['bank']
        try:
            with open('MockUserData.json') as f:
                data = json.load(f)
        except FileNotFoundError:
            return "Mock data file not found"
        
        manager.load_data(data)
        global user_info
        user_info = manager.get_user(username)
        bank_account = manager.get_bank_account(username)
        if bank_number != bank_account:
            return render_template('main_page.html', error_msg="User not found")
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
            return render_template('main_page.html', error_msg="User not found")
    if "types" in request.form:
        category = request.form['types']
        subscriptions_of_category = []
        if category == "All":
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
        elif category == "Entertainment":
            for s in user_info.subscriptionList:
                if s.type == "Entertainment":
                    subscriptions_of_category.append(s)
            return render_template('sub_page.html',user_name=user_info.name,subscriptions = [
                                    {
                                        'name': s.name,
                                        'type': s.type,
                                        'price': s.price,
                                        'usage': s.usage
                                    } for s in subscriptions_of_category
                                    ])
        elif category == "Productivity":
            for s in user_info.subscriptionList:
                if s.type == "Productivity":
                    subscriptions_of_category.append(s)
            return render_template('sub_page.html',user_name=user_info.name,subscriptions = [
                                    {
                                        'name': s.name,
                                        'type': s.type,
                                        'price': s.price,
                                        'usage': s.usage
                                    } for s in subscriptions_of_category
                                    ])
        elif category == "Games":
            for s in user_info.subscriptionList:
                if s.type == "Games":
                    subscriptions_of_category.append(s)
            return render_template('sub_page.html',user_name=user_info.name,subscriptions = [
                                    {
                                        'name': s.name,
                                        'type': s.type,
                                        'price': s.price,
                                        'usage': s.usage
                                    } for s in subscriptions_of_category
                                    ])
        elif category == "Utility":
            for s in user_info.subscriptionList:
                if s.type == "Utility":
                    subscriptions_of_category.append(s)
            return render_template('sub_page.html',user_name=user_info.name,subscriptions = [
                                    {
                                        'name': s.name,
                                        'type': s.type,
                                        'price': s.price,
                                        'usage': s.usage
                                    } for s in subscriptions_of_category
                                    ])
        elif category == "Other":
            for s in user_info.subscriptionList:
                if s.type == "Other":
                    subscriptions_of_category.append(s)
            return render_template('sub_page.html',user_name=user_info.name,subscriptions = [
                                    {
                                        'name': s.name,
                                        'type': s.type,
                                        'price': s.price,
                                        'usage': s.usage
                                    } for s in subscriptions_of_category
                                    ])

if __name__ == '__main__':
    app.run(debug=True)
