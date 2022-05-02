class MySQL:
    """ Interface com banco MySQL """

    DATA = []

    def match(self, db_type):
        return "MySQL" == db_type

    def list(self):
        return MySQL.DATA
    
    def save(self, item):
        MySQL.DATA.append(item)

    def update(self):
        print("Update with MySQL")

    def delete(self):
        print("Delete with MySQL")