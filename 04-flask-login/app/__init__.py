# Bismillah

from flask import Flask, g
import MySQLdb

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


from . import routes