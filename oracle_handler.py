class Oracle:
    """ Interface com banco Oracle """

    DATA = []

    def match(self, db_type):
        return "Oracle" == db_type

    def list(self, all: bool):
        if all:
            return Oracle.DATA
    
    def save(self, item):
        print(item)
        Oracle.DATA.append(item)

    def update(self):
        return ("Update with Oracle")

    def delete(self):
        return ("Delete with Oracle")