from flask_app  import app
from flask_app.models.dress import Dress
from flask import render_template, redirect, request

@app.route('/dresses')
def dresses_list():
    return render_template("dress_list.html")