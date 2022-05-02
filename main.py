from databasesHandlers.database_factory import DatabaseHandlerFactory

db = DatabaseHandlerFactory("Oracle")

print("Creating Oracle DB...")
db.save(item="Banana")
db.save(item="Jose")
db.save(item={"Name": "Jose", "Age": 15})
db.save(item=999)
db.fetch()

print("")

print("Switching to MySQL DB...")
db.change_db("MySQL")
db.save(item="Arvore")
db.save(item={"Hotel": "Trivago"})
db.fetch()

print("")

print("Switching back to Oracle...")
db.change_db("Oracle")
db.save(item="DvD")
db.fetch()