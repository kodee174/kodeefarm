from PySide2.QtSql import QSqlDatabase, QSqlQuery

class Database():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.db')
        self.db.open()
        self.query = QSqlQuery()
    
    def create(self, data):
        columns = []
        values = []
        for column, value in data.items():
            columns.append(column)
            values.append(value)
        self.query.exec_()
    def update(self):
        pass

    def delete(self):
        pass

    def filter(self, **kwargs):
        for key, value in kwargs.items():
             