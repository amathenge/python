from flask import Flask, render_template, g, request, session, redirect, url_for
from database import get_db
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def get_current_user():
    res = None
    if 'user' in session:
        user = session['user']
        db = get_db()
        cur = db.execute('select id, name, password, expert, admin from users where name = ?', [user])
        res = cur.fetchone()

    return res


@app.route('/')
def index():
    user = get_current_user()

    db = get_db()
    cur = db.execute("select q.id as qid, q.question_text as qtxt, q.asked_by_id qask, q.expert_id as qexp, u.name as uname, uu.name expname from questions q join users u on u.id = q.asked_by_id join users uu on uu.id = q.expert_id where q.answer_text is not null")
    res = cur.fetchall()

    return render_template('home.html', user=user, questions=res)

@app.route('/register', methods=['GET','POST'])
def register():
    user = get_current_user()
    if request.method == 'POST':
        n = request.form['name']
        p = request.form['password']
        hp = generate_password_hash(p, method='sha256')
        db = get_db()
        db.execute('insert into users (name, password, expert, admin) values (?, ?, ?, ?)', [n, hp, 0, 0])
        db.commit()

        session['user'] = n

        return redirect(url_for('index'))

    return render_template('register.html', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        n = request.form['name']
        p = request.form['password']
        db = get_db()
        conn = db.execute('select id, name, password, expert, admin from users where name = ?', [n])
        try:
            res = conn.fetchone()
        except:
            res = None
        if res is not None:
            if check_password_hash(res['password'], p):
                session['user'] = res['name']
                # del session['user']
                return redirect(url_for('index'))
            else:
                return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', user=None)

@app.route('/question/<question>')
def question(question):
    user = get_current_user()

    db = get_db()
    cur = db.execute("select q.id as qid, q.question_text as qtxt, q.answer_text as qans, q.asked_by_id qask, q.expert_id as qexp, u.name as uname, uu.name expname from questions q join users u on u.id = q.asked_by_id join users uu on uu.id = q.expert_id where q.id = ?", [question])
    res = cur.fetchone()

    return render_template('question.html', user=user, question=res)

@app.route('/answer/<question>', methods=['GET','POST'])
def answer(question):
    user = get_current_user()
    db = get_db()

    if request.method == 'POST':
        ans = request.form['answer']
        ans = ans.strip()
        if len(ans) == 0:
            return redirect(url_for('answer'))
        db.execute('update questions set answer_text = ? where id = ?',[ans, question])
        db.commit()
        return redirect(url_for('unanswered'))

    cur = db.execute("select q.id as qid, q.question_text as qtxt, q.asked_by_id qask, q.expert_id as qexp, u.name as uname, uu.name expname from questions q join users u on u.id = q.asked_by_id join users uu on uu.id = q.expert_id and uu.id = ? where (q.answer_text is null or q.answer_text = '') and q.id = ?", [user['id'], question])
    res = cur.fetchone()
    return render_template('answer.html', user=user, question=res)

@app.route('/ask', methods=['GET','POST'])
def ask():
    user = get_current_user()
    if user == None:
        return redirect(url_for('index'))
    if user['expert'] == 1 or user['admin'] == 1:
        return redirect(url_for('index'))

    if request.method == 'POST':
        txtQuestion = request.form['question']
        expert = request.form['eselect']

        db = get_db()
        db.execute('insert into questions (question_text, asked_by_id, expert_id) values (?, ?, ?)', [txtQuestion, user['id'], expert])
        db.commit()

        return redirect(url_for('ask'))

    db = get_db()
    cur = db.execute('select id, name, expert, admin from users where expert = 1')
    res = cur.fetchall()

    return render_template('ask.html', user=user, experts=res)

@app.route('/unanswered')
def unanswered():
    user = get_current_user()
    db = get_db()
    cur = db.execute("select q.id as qid, q.question_text as qtxt, q.asked_by_id qask, q.expert_id as qexp, u.name as uname, uu.name expname from questions q join users u on u.id = q.asked_by_id join users uu on uu.id = q.expert_id and uu.id = ? where (q.answer_text is null or q.answer_text = '')", [user['id']])
    res = cur.fetchall()

    return render_template('unanswered.html', user=user, questions=res)

@app.route('/users')
def users():
    user = get_current_user()

    db = get_db()
    cur = db.execute('select id, name, expert, admin from users')
    res = cur.fetchall()

    return render_template('users.html', user=user, users=res)

@app.route('/promote/<user_id>')
def promote(user_id):
    user = get_current_user()
    if user is None:
        return redirect(url_for('index'))

    db = get_db()
    cur = db.execute('select expert from users where id = ?', [user_id])
    res = cur.fetchone()
    if res['expert'] == 1:
        e = 0
    else:
        e = 1
    db.execute('update users set expert = ? where id = ?', [e, user_id])
    db.commit()

    return redirect(url_for('users'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

'''
 Don't use this code on PythonAnywhere.
if __name__ == '__main__':
    app.run(debug=True)
'''