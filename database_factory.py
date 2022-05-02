from mysql_handler import MySQL
from oracle_handler import Oracle

def interface(func):
    def wrapper(**kwargs):
        handler_function: function = eval(f"DatabaseHandlerFactory._db.{func.__name__}")
        # if kwargs:
        factory_args: list = [*kwargs]
        handler_args: list = handler_function.__code__.co_varnames
        keys: set = set(factory_args) & set(handler_args)
        kwargs = dict((key,value) for key, value in kwargs.items() if key in keys)
        return handler_function(**kwargs)
        # return handler_function
    return wrapper

class DatabaseHandlerFactory():

    _HANDLERS = [MySQL(), Oracle()]

    def __init__(self, db_type):
        DatabaseHandlerFactory._db = self._get_database(db_type)

    def _get_database(self, db_type):
        for db in DatabaseHandlerFactory._HANDLERS:
            if db.match(db_type):
                return db
    
    def change_db(self, db_type):
        for db in DatabaseHandlerFactory._HANDLERS:
            if db.match(db_type):
                DatabaseHandlerFactory._db=db
    
    @staticmethod
    @interface
    def list():
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