from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session

@app.route('/')
def main_page():
    return render_template('login.html')

@app.route('/dashboard')
def user_dashborad():
    return render_template('dashboard.html')

@app.route('/to_do')
def to_do_list():
    return render_template('to_do.html')

@app.route('/employees')
def employees():
    return render_template('employees.html')
    