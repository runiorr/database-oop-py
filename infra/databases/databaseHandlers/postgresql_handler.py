import psycopg2

class PostgreSQL:
    """ Interface com banco PostgreSQL """

    def __init__(self, database, user, password, host, port):
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cursor = None

    def execute(self, sql, vars=None):
        self.cursor.execute(query=sql, vars=vars)
    
    def commit(self):
        self.connection.commit()
        print("Changes have been commited.")
        
    def fetch(self, fetchAll=False):
        if fetchAll:
            data = self.cursor.fetchall()
            for d in data:
                print(f"Fetch response: {d}")
            return
        data = self.cursor.fetchone()
        print(f"Fetch response: {data}")
    
    def open(self):
        print("Openning connection...")
        self.cursor = self.connection.cursor()
    
    def close(self):
        print("Closing connection...")
        self.connection.close()