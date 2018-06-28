from flask import render_template, request

from . import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/alamatbaru')
def alamatbaru():
    r = request.args

    nama = r.get('nama')
    nis = r.get('nis')
    
    data = {
        "nm": nama,
        "ns": nis
    }
    return render_template('baru.html', dt=data)

@app.route('/form', methods=['POST','GET'])
def form_page():
    if request.method == 'POST':
        r = request.form

        nama = r.get('name')
        nis = r.get('nis')

        return "Namaku : {} dan NIS : {}".format(nama, nis)

    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')



