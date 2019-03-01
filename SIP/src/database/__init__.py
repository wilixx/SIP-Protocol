'''from database import database


db = database('client_data')
a = db.insert_records(['1', 'CLIENT', '1234'])
print(a)
records = db.print_records(['id'])
print(records)'''
from .database import database