class MySQL:
    """ Interface com banco MySQL """

    DATA = []

    def match(self, db_type):
        return "MySQL" == db_type

    @property
    def fetch(self):
        print(f"Fetching items from {__class__.__name__}...")
        quantity = f"MySQL database has {len(self.DATA)} items."
        listing = [f"Item {self.DATA.index(item)+1}: {str(item)}" for item in self.DATA]
        resp = f"Quantity: {quantity}\nItems: {listing}"
        print(resp)
    
    def save(self, item):
        print(f"Saving item: {item} to {__class__.__name__}")
        self.DATA.append(item)

    def update(self):
        return ("Update with MySQL")

    def delete(self):
        return ("Delete with MySQL")