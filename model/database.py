from PySide2.QtSql import QSqlDatabase

class Database():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data.db")
        self.db.open()