import psycopg2

class PostgreSQL:
    """ Interface com banco PostgreSQL """

    def __init__(self, database, user, password, host, port):
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cursor = None

    def execute(self, sql, vars=None):
        """ Execute sql query """
        self.cursor.execute(query=sql, vars=vars)
    
    def commit(self):
        """ Commit changes to DB \n 
        Closing without commiting is same as doing a rollback!"""
        self.connection.commit()
        print("Changes have been commited.")
        
    def fetchAll(self):
        """ Fetch all items from SELECT query """
        data = self.cursor.fetchall()
        for d in data:
            print(f"Fetch response: {d}")
    
    def fetchOne(self):
        """ Fetch first item from SELECT query """
        data = self.cursor.fetchone()
        print(f"Fetch response: {data}")
    
    def open(self):
        """ Open connection with PostgreSQL """
        print("Openning connection...")
        self.cursor = self.connection.cursor()
    
    def close(self):
        """ Close connection with PostgreSQL \n
        Closing without commiting is same as doing a rollback!"""
        print("Closing connection...")
        self.connection.close()