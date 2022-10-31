from flask_app.config.mysqlconnection import connectToMySQL

class Measurement:
    DB = "la_donna_bridal_atelier"
    def __init__(self, ms_data):
        self.id = ms_data['id']
        self.bride_id = []
        self.height = ms_data['height']
        self.waist = ms_data['waist']
        self.created_at = ms_data['created_at']
        self.updated_at = ms_data['updated_at']

    @classmethod
    def all_measurements(cls):
        query = "SELECT * FROM measurements;"
        return connectToMySQL(cls.DB).query_db(query)