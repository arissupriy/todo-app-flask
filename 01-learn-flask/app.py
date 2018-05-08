# Bismillah

from flask import Flask

# menginisialisasi nama apps (gunakan app = )
app = Flask(__name__)

# ini yang disebut route atau URL
@app.route('/')
def index():
    return 'Hello World'

@app.route('/namaku')
def namaku():
    return 'Nama saya adalah <b>Aris</b>'

# dynamic Route
@app.route('/namaku/<siapa>')
def nama_siapa(siapa):
    return 'Nama saya adalah <b>{}</b>'.format(siapa)

# function to be called first
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )