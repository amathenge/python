from application import app
from flask import render_template
from datetime import date

@app.route('/')
def index():
    td = date.today()
    return render_template('index.html', today = td)

