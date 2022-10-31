from flask_app import app
from flask_app.models import bride, dress, employee, measurement, order
from flask import render_template, redirect, request, session
import random
import string
import smtplib

@app.route('/')
def main_page():
    return render_template('login.html')

@app.route('/check_login', methods=["POST"])
def validate_login_info():
    login_data = {
        "email":request.form['email'],
        "password":request.form['password']
    }
    an_employee = employee.Employee.get_employee_by_email(login_data)
    print("---AN EMPLOYEE VALUE ----", an_employee)
    if not employee.Employee.validate_login(login_data, an_employee):
        return redirect('/')
    session['id'] = an_employee['id']
    session['first_name']=an_employee['first_name']
    session['last_name']=an_employee['last_name']
    return redirect('/dashboard')

@app.route('/check_registration', methods=["POST"])
def validate_registration():
    reg_data = {
        "registration_code":request.form['registration_code'],
        "email":request.form['email'],
        "password":request.form['password'],
        "password_confirm":request.form['password_confirm']
    }
    an_employee = employee.Employee.get_employee_by_email(reg_data)
    if not employee.Employee.validate_registration(reg_data, an_employee):
        return redirect('/')
    employee.Employee.update_employee_password(reg_data)
    
    return redirect('/login_after_register')


@app.route('/login_after_register')
def login_page_after_register():
    return render_template('login_after_reg.html')


@app.route('/dashboard')
def user_dashborad():
    return render_template('dashboard.html')

@app.route('/employees')
def employees():
    all_employees = employee.Employee.get_all_employees()
    return render_template('employees_list.html', all_employees = all_employees)
    
@app.route('/new_employee')
def add_new_empl_page():
    random_code =''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    print("----RANDOM GENERATED CODE: ----", random_code)

    return render_template('employee_add.html', random_code = random_code)

@app.route('/employee_add', methods=["POST"])
def add_empl_to_db():
    ee_data={
        "first_name":request.form['fname'],
        "last_name":request.form['lname'],
        "title":request.form['title'],
        "email":request.form['email'],
        "phone":request.form['phone'],
        "addr_street":request.form['addr_street'],
        "addr_city":request.form['addr_city'],
        "addr_state":request.form['addr_state'],
        "addr_zip":request.form['addr_zip'],
        "permission":request.form['permission'],
        "hire_date":request.form['hire_date'],
        "reg_code":request.form['reg_code']
    }

    # message = "You have been added to La Donna Bridal Atelier's employees list."
    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login("noormusheer@gmail.com", "PasswordHere")
    # server.sendmail("noormusheer@gmail.com", "noormusheer@aol.com", message)

    employee.Employee.add_employee_to_db(ee_data)
    return redirect('/employees')
