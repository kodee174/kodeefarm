from PySide2.QtSql import QSqlQuery
from database import Database

class Account():
    def __init__(self):
        self.db = Database()
        self.table = 'account'
        self.query = QSqlQuery
    def create(self, data):
        columns = []
        values = []
        for column, value in data.items():
            columns.append(column)
            values.append(value)
        self.query.exec_(self, 'INSERT INTO ' + self.table + '(' + columns.join(', ') + ') VALUES(' + values.join(', ') + ')')
    def update(self):
        pass

    def delete(self):
        pass