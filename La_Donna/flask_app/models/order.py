from flask_app.config.mysqlconnection import connectToMySQL

class Order:
    DB = "la_donna_bridal_atelier"
    def __init__(self, order_data):
        self.id = order_data['id']
        self.bride_id = order_data['bride_id']
        self.dress_id = order_data['dress_id']
        self.created_at = order_data['created_at']
        self.updated_at = order_data['updated_at']

    @classmethod
    def all_orders(cls):
        query = "SELECT * FROM orders;"
        return connectToMySQL(cls.DB).query_db(query)