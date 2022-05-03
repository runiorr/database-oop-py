from databases.databaseHandlers.database_factory import DatabaseFactory

db = DatabaseFactory("Athena")

db.open()
db.save(items=["Carro", "Moto"])
db.fetch()
db.close()

print("")

db.change_db("MySQL")
db.open()
db.save(items={"Hotel": "Trivago"})
db.fetch()
db.close()

print("")

db.change_db("Oracle")
db.open()
db.save(items="DvD")
db.fetch()
db.close()

print("")

db.change_db("Athena")
db.open()
db.save(items="Games")
db.fetch()
db.close()