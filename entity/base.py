from pony.orm import Database
HOST = "192.168.0.47"
PORT = 5432
DATABASE_NAME = "grants"
USER = "lubuntum"
PASS = "220922"
db = Database()
db.bind(provider='postgres', user=USER, password=PASS,
        host=HOST, database=DATABASE_NAME)
