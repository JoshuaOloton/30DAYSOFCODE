from flask import Blueprint

user = Blueprint('user',__name__)

from main.user import views