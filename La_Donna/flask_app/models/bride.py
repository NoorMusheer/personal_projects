from flask_app.config.mysqlconnection import connectToMySQL

class Bride:
    DB = "la_donna_bridal_atelier"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.wedding_date = data['wedding_date']
        self.other = data['other']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dress_id = []

    @classmethod
    def all_brides(cls):
        query = "SELECT * FROM brides;"
        return connectToMySQL(cls.DB).query_db(query)

