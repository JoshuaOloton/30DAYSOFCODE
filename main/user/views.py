from flask import render_template
from main.user import user

@user.route('/')
@user.route('/home')
def home():
    name = 'Joshua Oloton'
    return render_template('index.html', name=name)

@user.route('/home/<username>')
def home_greeting(username):
    return render_template('index.html', username=username)