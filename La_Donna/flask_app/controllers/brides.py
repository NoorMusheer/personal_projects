from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/brides')
def index():
    return render_template("brides_list.html")

@app.route('/new_bride')
def new_bride():
    return render_template("add_bride.html")

