from flask import Blueprint

post = Blueprint('post',__name__)

from main.post import views