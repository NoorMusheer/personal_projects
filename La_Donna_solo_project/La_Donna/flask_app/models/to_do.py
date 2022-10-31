from flask_app.config.mysqlconnection import connectToMySQL

class To_Do:
    DB = "la_donna_bridal_atelier"
    def __init__(self, tddata):
        self.id = tddata['id']
        self.notes = tddata['notes']
        self.date_due = tddata['date_due']
        self.created_at = tddata['created_at']
        self.updated_at = tddata['updated_at']

    @classmethod
    def all_to_do_items(cls):
        query = "SELECT * FROM to_do_items;"
        return connectToMySQL(cls.DB).query_db(query)

    @classmethod
    def new_task(cls, data):
        query = "INSERT INTO to_do_items (employee_id, notes, date_due, created_at, updated_at) VALUES (%(employee_id)s, %(notes)s, %(date_due)s, NOW(), NOW() );"
        return connectToMySQL(cls.DB).query_db(query, data)