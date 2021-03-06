from flask import Flask, render_template, request, url_for
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

@app.route('/')
def index():
    return render_template('index.html')