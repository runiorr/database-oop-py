class IDatabase:
    """ Interface para banco de dados """
    
    def _verify_connection(self):
        pass

    def fetch(self):
        pass
    
    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
    
    def open(self):
        pass
    
    def close(self):
        pass