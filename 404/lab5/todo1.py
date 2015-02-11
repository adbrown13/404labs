import sqlite3
from flask import Flask, render_template,g,request,url_for,session,flash,redirect, abort
import hashlib

DATABASE='tasksv2.db'
USERNAME='admin'
PASSWORD='admin'
SECRET_KEY='bahhumbug'

app=Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return '<h1> Welcome to my lab5 </h1>'

@app.route('/task',methods=['GET','POST'])
def task():
    if request.method=='POST':
        if not session.get('logged_in'):
            abort(401)
        category=request.form['category']
        priority=request.form['priority']
        description=request.form['description']
        addTask(category,priority,description)
        flash('New task has been added')
        return redirect(url_for('task'))

    return render_template('show_entries.html', tasks=query_db('select * from tasks'))

@app.route('/login',methods=['POST','GET'])
def login():
    error =None
    if request.method=='POST':
        users=query_db('select * from users where username=?',[request.form['username']])
        encrypted_pass = hashlib.sha1(request.form['password'].encode('utf-8')).hexdigest()
        if not users:
            error='Not a used username'
        
        elif  encrypted_pass!=users[0]['password']:
            error='Invalid Password'
        else:
            session['logged_in']=True
            flash('You are logged in...')
            return redirect(url_for('task'))
            
    return render_template('login.html',error=error)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in',None)
    flash('You are logged out...')
    return redirect(url_for('task'))  
@app.route('/signup',methods=['POST','GET'])
def signup():
    error =None
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        users=query_db('select * from users where username=?',[username])
        if users:
            error='taken username'
        else:
            encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
            query_db('insert into users(username,password) values (?,?)', [username, encrypted_pass], one=True)
            get_db().commit()
            return redirect(url_for('task'))
            
    return render_template('signup.html',error=error)

@app.route('/delete', methods=['POST'])
def delete():
    if not session.get('logged_in'):
        abort(401)
    removetask(request.form['ID'])
    return redirect(url_for('task'))
@app.route('/edit', methods=['POST'])
def edit():
    if not session.get('logged_in'):
        abort(401)
    ID=request.form['ID']   
    return render_template('edit.html', tasks=query_db('select * from tasks where ID = ?', [int(ID)],one=True))
    
def removetask(ID):
    query_db('delete from tasks where ID = ?', [int(ID)], one=True)
    get_db().commit()
def addTask(category,priority,description):
    query_db('insert into tasks(category,priority,description) values (?,?,?)', [category,int(priority),description], one=True)
    get_db().commit()
@app.route('/save', methods=['GET','POST'])
def save():
    ID=request.form['ID']
    
    category=request.form['category']
    priority=request.form['priority']
    description=request.form['description']         
    query_db('update tasks set category= ?, priority=?, description=? where ID=?', [category,int(priority),description,int(ID)], one=True)
    get_db().commit()
    return redirect(url_for('task'))
    
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db=g._database = sqlite3.connect(DATABASE)
        db.row_factory=sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection():
    db = getattr(g, '_database',None)
    if db is not None:
        db.close
def query_db(query,args=(),one=False):
    cur = get_db().cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return(rv[0] if rv else None) if one else rv

if __name__=='__main__':
    app.debug= True
    app.run()