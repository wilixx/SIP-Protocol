from database import database

db = database('clients', ['username', 'password'])
rows = db.insert_records(['user2', 'passw'])
print(rows)
rows = db.print_records()
print(rows)
rows = db.update_records({'username': 'user1'}, {'username': 'user2'})
print(rows)
rows = db.delete_records({'username': 'user2'})
print(rows)
