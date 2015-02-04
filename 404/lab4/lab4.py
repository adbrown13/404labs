#! /usr/bin/env python

from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DBFILE = 'ashleytasks.db'
conn = None
tasks = []

def get_conn():
    global conn
    if conn is None:
        conn = sqlite3.connect(DBFILE)
        conn.row_factory = sqlite3.Row
    return conn

@app.teardown_appcontext
def close_conn():
    global conn
    if conn != None:
        conn.close()

def query_db(query, args=(), one=False):
    cur = get_conn().cursor()
    cur.execute( query, args)
    r = cur.fetchall()
    cur.close()
    return (r[0] if r else None) if one else r

def add_task(category,priority,description):
    query_db('insert into task(category,priority,description) values(?,?,?)', [category,priority,description], one=True)
   # get_conn().commit()
# query_db('insert into task(priority) values(?)', [priority], one=True)
    #get_conn().commit()
  #  query_db('insert into task(description) values(?)', [description], one=True)
    get_conn().commit()

def print_tasks():
    tasks = query_db('select * from task')
    for task in tasks:
        print 'task(category): %s ' %task['category']
    print '%d tasks in total' %len(tasks)
    


@app.route('/')
def welcome():
    return '<h1>Welcome to 410 - Flask lab!</h1>'

@app.route('/task1', methods=['GET','POST'])
def task():
    #POST:
    if request.method == 'POST':
        category = request.form['category']
       # add_task(category=category)
        priority = request.form['priority']
       # add_task(category=priority)
        description = request.form['description']
        add_task(category,priority,description)
        return redirect(url_for('task'))
    #GET:
    resp = ''
    resp+= '''
    <form action = "" method = POST>
        <p>Category<input type=text name=category><p>
	<p>Priority<input type=number name=priority><p>
	<p>Description<input type=text name=description><p>
        <p><input type=submit value=Add></p>
    </form>
    '''
    #Show table
    resp+= '''
    <table border = "1" cellpadding="3">
        <tbody>
            <tr>
                <th>Category</th>
		<th>Priority</th>
		<th>Description</th>
            </tr>
    '''
    for task in query_db('select * from task'):
        resp+= '<tr><td>%s</td>' %(task['category'])
	resp+= '<td>%s</td>' %(task['priority'])
	resp+= '<td>%s</td></tr>' %(task['description'])
    resp+='''
        </tbody>
    </table>
    '''

    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()

