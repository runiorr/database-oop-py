from databasesHandlers.database_factory import DatabaseHandlerFactory

print("Creating Oracle DB...")
db = DatabaseHandlerFactory("Oracle")
db.save(item="Banana")
db.save(item="Jose")
db.save(item={"Name": "Jose", "Age": 15})
db.save(item=999)
db.list()

print("")

print("Switching to MySQL DB...")
db.change_db("MySQL")
db.save(item="Arvore")
db.save(item={"Hotel": "Trivago"})
db.list()

print("")

print("Switching back to Oracle...")
db.change_db("Oracle")
db.list()