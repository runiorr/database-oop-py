from databaseHandlers.db_factory import DatabaseHandlerFactory

db = DatabaseHandlerFactory("Athena")

db.open()
db.save(item="JOSE")
db.fetch()
db.close()

print("")

db.change_db("MySQL")
db.open()
db.save(item={"Hotel": "Trivago"})
db.fetch()
db.close()

print("")

db.change_db("Oracle")
db.open()
db.save(item="DvD")
db.fetch()
db.close()

print("")

db.change_db("Athena")
db.open()
db.save(item="Games")
db.fetch()
db.close()