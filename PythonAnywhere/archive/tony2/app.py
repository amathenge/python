from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.config['DEBUG'] = True

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'aamathenge.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'aamathenge'
app.config['MYSQL_PASSWORD'] = '0H1V$nkg12Be'
app.config['MYSQL_DB'] = 'aamathenge$plogin'

# Intialize MySQL
mysql = MySQL(app)

def get_db():
    return mysql.connection.cursor(MySQLdb.cursors.DictCursor)

def db_commit():
    mysql.connection.commit()

# index/home page
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/listmembers')
def list():
    cur = get_db()
    cur.execute('select id, firstname, lastname, email, notes from member')
    res = cur.fetchall()

    return render_template("listmember.html", datarows=res)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        cur = get_db()
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        notes = request.form['notes']
        cur.execute('insert into member (firstname, lastname, email, notes) values (%s, %s, %s, %s)',(firstname, lastname, email, notes,))
        db_commit()
        return redirect(url_for('list'))
    else:
        return render_template("addmember.html")

@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    if request.method == 'GET' and id:
        cur = get_db()
        cur.execute('select id, firstname, lastname, email, notes from member where id = %s', (id,))
        res = cur.fetchone()
        return render_template('editmember.html', member=res)
    else:
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        notes = request.form['notes']
        cur = get_db()
        cur.execute('update member set firstname = %s, lastname = %s, email = %s, notes = %s where id = %s', (firstname, lastname, email, notes, id,))
        db_commit()
        return redirect(url_for('list'))

@app.route('/delete<id>', methods=['GET','POST'])
def delete(id):
    cur = get_db()
    cur.execute('delete from member where id = %s',(id,))
    db_commit()
    return redirect(url_for('list'))


