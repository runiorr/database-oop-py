from infra.databases.database_factory import DatabaseFactory

db = DatabaseFactory("Oracle")

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
db.save(items=["DvD", "CD", "MP3", "Xbox"])
db.fetch()
db.close()

print("")

db.change_db("MySQL")
db.open()
db.save(items="Games")
db.fetch()
db.close()