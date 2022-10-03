from flask_app.config.mysqlconnection import connectToMySQL

class Bride:
    DB = "la_donna_bridal_atelier_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dress = []

    @classmethod
    def show_all_brides(cls):
        query = "SELECT * FROM brides;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def add_bride(cls, data):
        query = "INSERT INTO brides (first_name, last_name, email, phone, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s, %(email)s, %(phone)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)