from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/dresses')
def dresses_list():
    return render_template("dresses.html")