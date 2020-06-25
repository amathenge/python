from flask import Flask, request, session, render_template, g
import sqlite3
from datetime import datetime

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'jUkkd7*&4,dfYkkd\dfmodijh$$(ya!!2'

def connect_db():
    sql = sqlite3.connect('/home/aamathenge/tracker/food_log.db')
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

@app.route('/', methods=['GET','POST'])
def index():
    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        database_date = datetime.strptime(date, '%Y-%m-%d')
        final_database_date = datetime.strftime(database_date, '%Y%m%d')
        # pretty_date = datetime.strftime(database_date, '%B %d, %Y')

        db.execute('insert into log_date (entry_date) values (?)', [final_database_date])
        db.commit()

    # cur = db.execute('select entry_date from log_date order by entry_date desc')
    cur = db.execute('''select log_date.entry_date, sum(food.protein) as protein, sum(food.carbohydrates) as carbohydrates,
        sum(food.fat) as fat, sum(food.calories) as calories
        from log_date
        left join food_date on food_date.log_date_id = log_date.id
        left join food on food_date.food_id = food.id
        group by log_date.entry_date
        order by log_date.entry_date desc''')
    res = cur.fetchall()

    p_res = []

    for item in res:
        entry = {}
        entry['entry_date'] = str(item['entry_date'])
        d = datetime.strptime(str(item['entry_date']), '%Y%m%d')
        entry['pretty_date'] = datetime.strftime(d, '%B %d, %Y')
        entry['protein'] = item['protein']
        entry['carbohydrates'] = item['carbohydrates']
        entry['fat'] = item['fat']
        entry['calories'] = item['calories']
        p_res.append(entry)


    return render_template('home.html', results=p_res)


@app.route('/view/<date>', methods=['GET','POST'])
def view(date):
    db = get_db()
    cur = db.execute('select id, entry_date from log_date where entry_date = ?', [date])
    res = cur.fetchone()

    if request.method == 'POST':
        db.execute('insert into food_date (food_id, log_date_id) values (?, ?)',
            [request.form['food-select'], res['id']])
        db.commit()

    dt = datetime.strptime(str(res['entry_date']), '%Y%m%d')
    p_date = datetime.strftime(dt, '%B %d, %Y')
    e_date = str(res['entry_date'])

    cur_food = db.execute('select id, name from food')      # for the dropdown list
    res_food = cur_food.fetchall()

    cur_log = db.execute('select food.name, food.protein, food.carbohydrates, food.fat, food.calories from log_date join food_date on food_date.log_date_id = log_date.id join food on food_date.food_id = food.id where log_date.entry_date = ?', [date])
    res_log = cur_log.fetchall()

    totals = {}
    totals['protein'] = 0
    totals['carbohydrates'] = 0
    totals['fat'] = 0
    totals['calories'] = 0

    for food in res_log:
        totals['protein'] += food['protein']
        totals['carbohydrates'] += food['carbohydrates']
        totals['fat'] += food['fat']
        totals['calories'] += food['calories']

    return render_template('day.html', date=p_date, foods=res_food, results=res_log, totals=totals, edate=e_date)

@app.route('/food', methods=['GET','POST'])
def food():
    db = get_db()
    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = (protein * 4) + (carbohydrates * 4) + (fat * 9)

        db.execute('insert into food (name, protein, carbohydrates, fat, calories) values (?, ?, ?, ?, ?)',
            [name, protein, carbohydrates, fat, calories])
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fat, calories from food')
    res = cur.fetchall()

    return render_template('add_food.html', results=res)