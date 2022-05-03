from databaseHandlers.IDatabase import IDatabase

class Athena(IDatabase):
    """ Interface com banco Athena """

    def __init__(self):
        super().__init__()

    def match(self, db_type):
        return "Athena" == db_type