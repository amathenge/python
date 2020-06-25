from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

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

# we have a database test with two columns
# id = primary key, auto_increment
# data = varchar(1024)

@app.route('/')
def index():
    return render_template('index.html', pageHeading="Home Page")

@app.route('/data')
def data():
    cur = get_db()
    cur.execute('select id, data from test')
    res = cur.fetchall()
    return render_template('data.html', datarows=res, pageHeading="Data Display")

@app.route('/add', methods=['GET','POST'])
def add():
    msg = 'Add data to database'
    if request.method == 'POST':
        data = request.form['data']
        if data.strip() == '':
            msg = 'data cannot be blank'
            return render_template('add.html', pageHeading="Add Data", pageMessage=msg)
        else:
            cur = get_db()
            cur.execute('insert into test (data) values (%s)',(data,))
            db_commit()
            return redirect(url_for('data'))

    return render_template('add.html', pageHeading="Add Data", pageMessage=msg)


@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    if request.method == 'POST':
        id = request.form['id']
        data = request.form['data']
        if data.strip() == '':
            return redirect(url_for('data'))
        cur = get_db()
        cur.execute('update test set data = %s where id = %s', (data, id,))
        db_commit()
        return redirect(url_for('data'))
    else:
        cur = get_db()
        cur.execute('select id, data from test where id = %s', (id,))
        res = cur.fetchone()
        return render_template('edit.html', pageHeading="Edit Data", pageMessage='', rowData=res)


@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    cur = get_db()
    cur.execute('delete from test where id = %s',(id,))
    db_commit()
    return redirect(url_for('data'))





