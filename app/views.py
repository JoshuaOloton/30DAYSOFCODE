from app import app
from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    name = 'Joshua Oloton'
    return render_template('index.html', name=name)

@app.route('/home/<username>')
def home_greeting(username):
    return render_template('index.html', username=username)