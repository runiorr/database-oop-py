from databases.interfaces.IDatabase import IDatabase

class Database(IDatabase):
    """ Interface com banco Oracle """

    def __init__(self):
        self.db_name = self.__class__.__name__
        self.connection = 0
        self.data = []
    
    def _verify_connection(self):
        if self.connection == 0:
            raise Exception(f"{self.db_name} connection is closed. Open to interact with it.")

    @property
    def fetch(self):
        self._verify_connection()
        print(f"Fetching items from {self.db_name}...")
        listing = [f"Item {self.data.index(item)+1}: {str(item)}" for item in self.data]
        resp = f"{self.db_name} has {len(self.data)} item(s) - Item(s): {listing}"
        print(resp)
    
    def save(self, item):
        self._verify_connection()
        self.data.append(item)
        print(f"Saved item '{item}' to {self.db_name}")

    def update(self):
        self._verify_connection()
        return (f"Update with {self.db_name}")

    def delete(self):
        self._verify_connection()
        return (f"Delete with {self.db_name}")
    
    @property
    def open(self):
        print(f"Openning {self.db_name} connection...")
        self.connection = 1
    
    @property
    def close(self):
        print(f"Closing {self.db_name} connection...")
        self.connection = 0