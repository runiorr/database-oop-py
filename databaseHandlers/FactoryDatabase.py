from databaseHandlers.mysql_handler import MySQL
from databaseHandlers.oracle_handler import Oracle
from databaseHandlers.athena_handler import Athena

def interface(func):
    def wrapper(**kwargs):
        handler_function: function = eval(f"DatabaseFactory.database.{func.__name__}")
        if kwargs:
            factory_args: list = [*kwargs]
            handler_args: list = handler_function.__code__.co_varnames
            keys: set = set(factory_args) & set(handler_args)
            kwargs = dict((key,value) for key, value in kwargs.items() if key in keys)
            return handler_function(**kwargs)
        return handler_function
    return wrapper

class DatabaseFactory:

    HANDLERS = [MySQL(), Oracle(), Athena()]

    def __init__(self, db_type):
        DatabaseFactory.database = self.get_database(db_type)

    @staticmethod
    def get_database(db_type):
        for db in DatabaseFactory.HANDLERS:
            if db.match(db_type):
                return db
        raise Exception(f"Database {db_type} not found.")
    
    @staticmethod
    def change_db(db):
        if DatabaseFactory.database.db_name == db:
            raise Exception(f"{db} is already connected")
        if DatabaseFactory.database.connection == 1:
            raise Exception(f"Close {DatabaseFactory.database.db_name} connection before switch to {db}")
        DatabaseFactory.database = DatabaseFactory.get_database(db)
    
    @staticmethod
    @interface
    def fetch():
        pass
    
    @staticmethod
    @interface
    def save():
        pass

    @staticmethod
    @interface
    def update():
        pass

    @staticmethod
    @interface
    def delete():
        pass

    @staticmethod
    @interface
    def open():
        pass

    @staticmethod
    @interface
    def close():
        pass