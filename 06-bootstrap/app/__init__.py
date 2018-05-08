# Bismillah

from flask import Flask, g
import MySQLdb
import os

# menginisialisasi nama apps (gunakan app = )
app = Flask(__name__)

app.secret_key = 'iniadalahkoderahasialatihanngoding'

# Before request URL
@app.before_request
def db_connect():
    # Database Configuration with mysql
    g.conn = MySQLdb.connect(
        host = 'localhost',
        user = 'admin',
        passwd = 'qscwdvefb',
        db = 'todoapp',
        charset='utf8',
        use_unicode=True)
    g.cursor = g.conn.cursor()

# After Request Process
@app.after_request
def db_disconnect(response):
    g.cursor.close()
    g.conn.close()
    return response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
app.static_folder = os.path.join(BASE_DIR, 'static')

from . import routes