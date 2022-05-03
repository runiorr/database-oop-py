from databases.databaseHandlers.mysql_handler import MySQL
from databases.databaseHandlers.oracle_handler import Oracle
from databases.databaseHandlers.athena_handler import Athena

def interface(func):
    def wrapper(**kwargs):
        handler_function: function = eval(f"DatabaseFactory.database.{func.__name__}")
        if kwargs:
            # factory_args: list = [*kwargs]
            # handler_args: list = handler_function.__code__.co_varnames
            # keys: set = set(factory_args) & set(handler_args)
            # kwargs = dict((key,value) for key, value in kwargs.items() if key in keys)
            return handler_function(kwargs.get(*kwargs))
        return handler_function
    return wrapper

class DatabaseFactory:
    """ Database factory """

    HANDLERS = [MySQL(), Oracle(), Athena()]

    def __init__(self, db_type):
        DatabaseFactory.database = self.__get_database(db_type)

    @staticmethod
    def __get_database(db_type):
        for db in DatabaseFactory.HANDLERS:
            if db.match(db_type):
                return db
        raise Exception(f"Database {db_type} not found.")
    
    @staticmethod
    def change_db(db):
        """ Switch database being used """
        if DatabaseFactory.database.db_name == db:
            raise Exception(f"{db} is already connected.")
        if DatabaseFactory.database.connection == 1:
            if db not in DatabaseFactory.HANDLERS:
                raise Exception(f"Close {DatabaseFactory.database.db_name} connection and choose an existing database.")
            raise Exception(f"Close {DatabaseFactory.database.db_name} connection before switch to {db}.")
        DatabaseFactory.database = DatabaseFactory.__get_database(db)
    
    @staticmethod
    @interface
    def fetch():
        """ Get all items storaged in database """
        pass
    
    @staticmethod
    @interface
    def save():
        """ Save an item in the database """
        pass

    @staticmethod
    @interface
    def update():
        """ Update an item in the database """
        pass

    @staticmethod
    @interface
    def delete():
        """ Delete an item in the database """
        pass

    @staticmethod
    @interface
    def open():
        """ Open a connection with the chosen database """
        pass

    @staticmethod
    @interface
    def close():
        """ Close the connection with the chosen database """
        pass