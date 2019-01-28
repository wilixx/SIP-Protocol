import database

db = database.database()
query = db.display_data()
print(db.execute_statement(query))
