from flask_app.config.mysqlconnection import connectToMySQL

class Dress: 
    def __init__(self,dress_data):
        self.id = dress_data['id']