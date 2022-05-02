from database_factory import DatabaseHandlerFactory

db = "Oracle"

db_handler = DatabaseHandlerFactory(db)

db_handler.save(item=2)

db_handler.list(all=True)