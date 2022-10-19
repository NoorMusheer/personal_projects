from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

class Dress: 
    DB = "la_donna_bridal_atelier"
    def __init__(self,dress_data):
        self.id = dress_data['id']
        self.employee_id = dress_data['employee_id']
        self.name = dress_data['name']
        self.style = dress_data['style']
        self.color = dress_data['color']
        self.fabric = dress_data['fabric']
        self.other = dress_data['other']
        self.created_at = dress_data['created_at']
        self.updated_at = dress_data['updated_at']

    @classmethod
    def all_dresses(cls):
        query = "SELECT * FROM dresses;"
        return connectToMySQL(cls.DB).query_db(query)