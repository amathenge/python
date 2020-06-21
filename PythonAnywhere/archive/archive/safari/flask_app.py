from flask import Flask, request, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisxy.9876dm =#@!'

def connect_db():
    sql = sqlite3.connect('/home/aamathenge/safari/data.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['GET', 'POST'], defaults={'name': 'Tony'})
@app.route('/<string:name>')
def index(name):
    session['name'] = name
    try:
        user = session['user']
    except:
        user = 'Not logged in'

    return render_template('home.html', name=name, psess=session['name'], user=user, apppath=app.instance_path, rootpath=app.root_path)

@app.route('/query', methods=['GET','POST'])
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return 'You are {} the person who live in {}'.format(name, location)

@app.route('/theform', methods=['GET','POST'])
def theform():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    sessionName = session['name']

    db = get_db()
    db.execute('insert into users (name, location) values (?, ?)', [name, location])
    db.commit()

    return '<h1>Hello {} you are from {} - this stuff came from the form [{}]'.format(name,location,sessionName)

@app.route('/login', methods=['GET','POST'])
def login():
    retString = '''
        <form name="login" method="POST" action="/confirmlogin">
            <input type="text" name="user" placeholder="username">
            <input type="password" name="pwd">
            <input type="submit" value="login">
        </form>
    '''
    return retString

@app.route('/confirmlogin', methods=['GET','POST'])
def confirmlogin():
    user = request.form['user']
    pwd = request.form['pwd']
    session['user'] = user
    session['pwd'] = pwd
    dString = '<strong>You have successfully logged in as user: {} with pass: {}'.format(user,pwd)
    return dString

@app.route('/logout', methods=['GET','POST'])
def logout():
    session['user'] = 'Null'
    return '<h1>You have successfully logged out</h1>'

@app.route('/dictstuff', methods=['GET','POST'])
def dictstuff():
    thedict = {'one': 1, 'two': 'justice', 'three': (1, 2), 'four': 'user'}
    return render_template('dict.html', thedict=thedict)

@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    res = cur.fetchall()
    resString = '''
        <table><tr><th>ID</th><th>Name</th><th>Location</th></tr>
    '''
    for item in res:
        resString += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(item['id'],item['name'],item['location'])
    resString += "</table>"
    return resString

@app.route('/showdata')
def showdata():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    res = cur.fetchall()
    return render_template('data.html', rowdata=res)


