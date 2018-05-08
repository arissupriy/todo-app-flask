# Bismillah

from flask import Flask, render_template

# menginisialisasi nama apps (gunakan app = )
app = Flask(__name__)

# ini yang disebut route atau URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/namaku')
def namaku():
    nama = 'Aris Supriyanto'
    kelas = 'X RPL'
    nis = '12345'
    return render_template('namaku.html', nama=nama, kelas=kelas, nis=nis)

# dynamic Route
@app.route('/namaku/<siapa>')
def nama_siapa(siapa):
    nama = siapa
    return render_template('namaku.html', nama=nama)

