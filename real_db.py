from infra.databases.databaseHandlers.postgresql_handler import PostgreSQL 

db = PostgreSQL(database="docker", user='docker', password='docker', host='0.0.0.0', port= '80')

db.open()

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS people(
                ID SERIAL PRIMARY KEY,
                NAME VARCHAR(255) NOT NULL,
                AGE INT NOT NULL,
                ADDRESS VARCHAR(255) NOT NULL)"""
db.execute(sql=CREATE_TABLE)

INSERT_SQL = "INSERT INTO people (NAME, AGE, ADDRESS) VALUES (%s, %s, %s)"
INSERT_VARS = ("Pablo", 45, "Paraná")
# db.execute(sql=INSERT_SQL, vars=INSERT_VARS)

# SELECT_SQL = "SELECT * FROM people p WHERE p.name='Thalles'"
SELECT_SQL = "SELECT * FROM people"
db.execute(sql=SELECT_SQL)
db.fetchAll()
db.fetchOne()

db.commit()
db.close()