from databaseHandlers.db_interface import Database

class Oracle(Database):
    """ Interface com banco Oracle """

    def __init__(self):
        super().__init__()

    def match(self, db_type):
        return "Oracle" == db_type