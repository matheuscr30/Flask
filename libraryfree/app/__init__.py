from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

from app.controllers import users
