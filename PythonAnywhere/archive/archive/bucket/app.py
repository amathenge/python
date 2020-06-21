from flask import Flask, render_template, url_for, request
from werkzeug import generate_password_hash, check_password_hash
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'aamathenge'
app.config['MYSQL_DATABASE_PASSWORD'] = '0H1V$nkg12Be'
app.config['MYSQL_DATABASE_DB'] = 'aamathenge$bucketlist'
app.config['MYSQL_DATABASE_HOST'] = 'aamathenge.mysql.pythonanywhere-services.com'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        nm = request.form['inputName']
        em = request.form['inputEmail']
        pw = request.form['inputPassword']

        if nm and em and pw:
            conn = mysql.connect()
            cur = conn.cursor()
            hp = generate_password_hash(pw)
            cur.callproc('sp_createUser',(nm,em,hp))
            return json.dumps({'html': '<p>All fields entered</p>'})
        else:
            return json.dumps({'html': '<p>Some/all fields are missing</p>'})

    return render_template("signup.html")

