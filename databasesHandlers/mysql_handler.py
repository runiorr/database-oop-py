from databasesHandlers.db_interface import Database

class MySQL(Database):
    """ Interface com banco MySQL """

    def __init__(self):
        super().__init__()

    def match(self, db_type):
        return "MySQL" == db_type