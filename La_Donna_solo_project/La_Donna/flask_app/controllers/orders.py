from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session


@app.route('/orders')
def orders_page():
    all_orders = order.Order.all_orders()
    return render_template('orders_list.html', all_orders = all_orders)

@app.route('/new_order')
def new_order():
    return render_template('order_add.html')

@app.route('/order_add', methods=["POST"])
def add_order_to_db():
    data={
        "employee_id":session['id'],
        "dress_id":request.form['dress_id'],
        "bride_id":request.form['bride_id'],
        "notes":request.form['notes'],
    }
    order.Order.add_order_to_db(data)
    return redirect('/orders')