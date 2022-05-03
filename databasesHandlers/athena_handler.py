from databasesHandlers.db_interface import Database

class Athena(Database):
    """ Interface com banco Athena """

    def __init__(self):
        super().__init__()

    def match(self, db_type):
        return "Athena" == db_type