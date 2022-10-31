from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/dresses')
def dresses_list():
    all_dresses = dress.Dress.all_dresses()
    return render_template("dresses_list.html", all_dresses = all_dresses)

@app.route('/new_dress')
def add_a_dress():
    return render_template('dress_add.html')

@app.route('/dress_add', methods=["POST"])
def add_dress_to_db():
    data={
        "employee_id":1,
        "name":request.form['dress_name'],
        "style":request.form['style'],
        "color":request.form['color'],
        "fabric":request.form['fabric'],
        "other":request.form['other']
    }
    dress.Dress.add_dress(data)
    return redirect('/dresses')