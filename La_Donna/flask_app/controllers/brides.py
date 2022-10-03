from flask_app import app
from flask_app.models.bride import Bride
from flask import render_template, redirect, request

@app.route('/')
def index():
    brides = Bride.show_all_brides()
    return render_template("index.html", brides=brides)

@app.route('/new_bride')
def new_bride():
    return render_template("add_bride.html")

@app.route('/add_bride', methods=["POST"])
def add_bride():
    data ={
        "first_name":request.form['fname'],
        "last_name":request.form['lname'],
        "email":request.form['email'],
        "phone":request.form['phone']
    }
    Bride.add_bride(data)
    return redirect('/')