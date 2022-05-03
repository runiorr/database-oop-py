from databases.Database import Database

class PostgreSQL(Database):
    """ Interface com banco PostgreSQL """

    def __init__(self):
        super().__init__()

    def match(self, db_type):
        return "PostgreSQL" == db_type