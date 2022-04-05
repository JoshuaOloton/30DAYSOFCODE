from app import app
from flask import render_template

@app.route('/')
def home():
    name = 'Joshua Oloton'
    return render_template('index.html', name=name)