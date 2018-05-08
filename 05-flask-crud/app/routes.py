from app import app
from flask import render_template, request, flash, redirect, url_for, g, session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from app.libs import login_required

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        req = request.form
        username = req['username']
        password = req['password']

        q_select = ''' SELECT * FROM users WHERE username = "{}"; '''.format(username)

        g.cursor.execute(q_select)
        select = g.cursor.fetchone()
        
        if select  == None:
            flash('Username tidak ditemukan')
            return redirect(url_for('login'))

        check_password = check_password_hash(select[3], password)
        if not check_password:
            flash('Password yang anda masukkan salah')
            return redirect(url_for('login'))

        session['user'] = {
            "id": select[0],
            "username": select[2]
        }
        
        return redirect(url_for('admin'))

    return render_template('user/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        req = request.form
        name = req['name']
        username = req['username']
        password = req['password']
        created = datetime.datetime.now()
        
        hash_password = generate_password_hash(password)

        query = ''' INSERT INTO users (username, name, password, created) VALUES ("{}","{}","{}","{}") '''.format(username, name, hash_password, created)
        
        g.cursor.execute(query)
        g.conn.commit()

        flash('berhasil melakukan pendaftaran')
        return redirect(url_for('register'))
    
    return render_template('user/register.html')

@app.route('/logout')
def logout():
    session['user'] = None
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    username = session['user']['username']
    user_id = session['user']['id']

    query = ''' SELECT * FROM todo WHERE user_id = {} '''.format(user_id)

    g.cursor.execute(query)
    select = g.cursor.fetchall()

    return render_template('admin/index.html', username=username, todos=select)

@app.route('/add-todo', methods=['POST'])
@login_required
def create_todo():
    req = request.form
    name = req['name']
    
    user_id = session['user']['id']
    now = datetime.datetime.now()

    query = ''' INSERT INTO todo (name, user_id, status, created) VALUES("{}","{}","{}","{}") '''.format(name, user_id, 0, now)
    
    g.cursor.execute(query)
    g.conn.commit()

    flash('Berhasil menyimpan jadwal')
    return redirect(url_for('admin'))

@app.route('/delete-todo', methods=['POST'])
@login_required
def delete_todo():
    req = request.form
    id = req['id']

    query = ''' DELETE FROM todo WHERE id = {} '''.format(id)
    g.cursor.execute(query)
    g.conn.commit()
    
    flash('Berhasil menghapus jadwal')
    return redirect(url_for('admin'))

@app.route('/edit-todo', methods=['POST'])
@login_required
def edit_todo():
    req = request.form
    id = req['id']
    name = req['name']

    query = ''' UPDATE todo SET name="{}" WHERE id = {} '''.format(name, id)
    g.cursor.execute(query)
    g.conn.commit()
    
    flash('Berhasil Memperbarui jadwal')
    return redirect(url_for('admin'))

@app.route('/finish-todo', methods=['POST'])
@login_required
def finish_todo():
    req = request.form
    id = req['id']

    query = ''' UPDATE todo SET status="{}" WHERE id = {} '''.format(1, id)
    g.cursor.execute(query)
    g.conn.commit()
    
    flash('Berhasil Memperbarui jadwal')
    return redirect(url_for('admin'))
    

@app.route('/todo/<id>/edit')
@login_required
def update_todo(id):
    id = id
    query = ''' SELECT * FROM todo WHERE id={} '''.format(id)

    g.cursor.execute(query)
    select = g.cursor.fetchone()

    return render_template('admin/edit-todo.html', data=select)


