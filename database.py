import sqlite3

class database:

    conn = sqlite3.connect('clients.db')

    c = conn.cursor()

    table_name = 'clients'  #Get table name at run time, can also put in a fixed value
    columns = [ 'client_name', 'client_network_name', 'subject' ]

    def create_table(self):
        create_statement = 'CREATE TABLE ' + self.table_name + ' ('
        for column in self.columns:
            create_statement += column + ' text,'
        create_statement = create_statement.rstrip(',')
        create_statement += ')' + ";"
        return create_statement

    def display_data(self, where_clause={}):
        #size of columns and values should be the same
        display_statement = 'SELECT '
        if len(where_clause) != 0:
            for column in self.columns:
                display_statement += column + ','
            display_statement = display_statement.rstrip(',') + ' '
            display_statement += 'FROM ' + self.table_name
            if len(where_clause.items()) != 0:
                display_statement += ' WHERE '
                for key, value in where_clause.items():
                    display_statement += key + '=\"' + value + '\",'
                display_statement = display_statement.rstrip(',') + ";"
        else:
            display_statement += '* FROM ' + self.table_name + ";"
        return display_statement

    def insert_data(self, client_name, client_network_name, subject):
        insert_statement = 'INSERT INTO ' + self.table_name + ' VALUES(\"' + client_name + '\",\"' + client_network_name + '\",\"' + subject + '\")' + ";"
        return insert_statement

    def update_data(self, where_clause={}, update_clause={}):
        if len(where_clause) != 0:
            update_statement = 'UPDATE ' + self.table_name
            update_statement += ' SET '
            if len(where_clause) != 0:
                for key, value in update_clause.items():
                    update_statement += key + '=\"' + value + '\",'
                update_statement = update_statement.rstrip(',')
            update_statement += ' WHERE '
            for key, value in where_clause.items():
                update_statement += key + '=\"' + value + '\",'
            update_statement = update_statement.rstrip(',') + ";"
        return update_statement

    def delete_data(self, where_clause={}):
        delete_statement = 'DELETE FROM ' + self.table_name + ' WHERE '
        for key, value in where_clause.items():
            delete_statement += key + '=\"' + value + '\",'
        delete_statement = delete_statement.rstrip(',') + ";"
        return delete_statement

    def execute_statement(self, statement):
        self.c.execute(statement)
        rows = self.c.fetchall()
        return rows

    def disconnect_from_database(self):
        self.conn.close()

DB = database()
statement = DB.create_table()
print('Created table')
statement1 = DB.insert_data('CLIENT1', 'client1', 'file_name')
print('Inserted data into table')
statement2 = DB.insert_data('CLIENT2', 'client2', 'file_name')
print('Inserted data into table')
statement3 = DB.display_data()
print('Display data from table')
statement4 = DB.display_data({'client_name': '*CLIENT*'})
print('Display data from table')
statememt5 = DB.update_data({'subject': 'files'}, {'client_name': '*CLIENT1*'})
statement6 = DB.delete_data({'*CLIENT1*': 'client1'})
print(statement)
print(statement1)
print(statement2)
print(statement3)
print(statement4)
print(statement5)
print(statement6)
DB.execute_statement(statement5)
DB.disconnect_from_database()
