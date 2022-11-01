from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session


@app.route('/orders')
def orders_page():
    active = {
        "status":"active"
    }
    active_orders = order.Order.orders_by_status(active)
    archived = {
        "status":"archived"
    }
    archived_orders = order.Order.orders_by_status(archived)
    return render_template('orders_list.html', active_orders = active_orders, archived_orders = archived_orders)

@app.route('/archive_order/<int:id>')
def update_to_archived(id):
    order.Order.update_status_to_archive(id)
    return redirect('/orders')

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
        "status":"active"
    }
    order.Order.add_order_to_db(data)
    return redirect('/orders')