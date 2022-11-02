from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/brides')
def index():
    all_brides = bride.Bride.all_brides()
    return render_template("brides_list.html", all_brides = all_brides)

@app.route('/new_bride')
def new_bride():
    return render_template("bride_add.html")

@app.route('/bride_add', methods=['POST'])
def add_bride_to_db():
    data={
        "first_name":request.form['fname'],
        "last_name":request.form['lname'],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "wedding_date":request.form['wedding_date'],
        "other":request.form['other']
    }
    bride.Bride.add_a_bride(data)
    return redirect('/brides')

@app.route('/bride_edit/<int:id>')
def edit_bride_page(id):
    bride_info = bride.Bride.get_bride_by_id(id)
    return render_template('brides_edit.html', bride = bride_info)

