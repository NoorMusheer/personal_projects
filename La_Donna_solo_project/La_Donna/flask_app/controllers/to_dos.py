from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order, to_do
from flask import render_template, redirect, request, session

@app.route('/task_list')
def to_do_page():
    all_tasks = to_do.To_Do.all_to_do_items()
    return render_template('to_do_list.html', all_tasks = all_tasks)

@app.route('/task_new')
def add_new_task_page():
    return render_template('to_do_add.html')

@app.route('/task_add', methods=["POST"])
def add_task_to_db():
    data={
        "employee_id":1,
        "notes":request.form['notes'],
        "date_due":request.form['date_due']
    }
    to_do.To_Do.new_task(data)
    return redirect('/task_list')

