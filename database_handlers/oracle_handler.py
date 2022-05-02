class Oracle:
    """ Interface com banco Oracle """

    DATA = []

    def match(self, db_type):
        return "Oracle" == db_type

    @property
    def list(self):
        print(f"Fetching items from {__class__.__name__}...")
        quantity = f"Oracle database has {len(self.DATA)} items."
        listing = [f"Item {self.DATA.index(item)+1}: {str(item)}" for item in self.DATA]
        resp = f"Quantity: {quantity}\nItems: {listing}"
        print(resp)
    
    def save(self, item):
        print(f"Saving item: {item} to {__class__.__name__}")
        self.DATA.append(item)

    def update(self):
        return ("Update with Oracle")

    def delete(self):
        return ("Delete with Oracle")