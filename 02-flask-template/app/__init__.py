from flask import Flask
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
STATIC = os.path.join(BASE_DIR, 'static')
app.static_folder = STATIC

from . import routes
