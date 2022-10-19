from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class Employee: 
    DB = "la_donna_bridal_atelier"
    def __init__(self, ee_data):
        self.id = ee_data['id']
        self.first_name = ee_data['first_name']
        self.last_name = ee_data['last_name']
        self.title = ee_data['title']
        self.email = ee_data['email']
        self.phone= ee_data['phone']
        self.addr_street = ee_data['addr_street']
        self.city = ee_data['city']
        self.state = ee_data['state']
        self.zip = ee_data['zip']
        self.permission = ee_data['permission']
        self.hire_date = ee_data['hire_date']
        self.password = ee_data['password']
        self.created_at = ee_data['created_at']
        self.updated_at = ee_data['updated_at']

    @classmethod
    def get_all_employees(cls):
        query = "SELECT * FROM employees;"
        return connectToMySQL(cls.DB).query_db(query)