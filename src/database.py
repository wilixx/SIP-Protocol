import sqlite3

class database:

    table_name = 'clients'
    columns = [ 'client_name', 'client_network_name', 'subject' ]
    conn = ''
    c = ''

    def __init__(self):#table_name=None, columns=None):
        self.conn = sqlite3.connect('../database/clients.db')
        self.c = self.conn.cursor()
        #self.table_name = table_name
        #self.columns = columns

    def create_table(self):
        #Should execute only once
        create_statement = 'CREATE TABLE ' + self.table_name + ' ('
        for column in self.columns:
            create_statement += column + ' text,'
        create_statement = create_statement.rstrip(',')
        create_statement += ')' + ";"
        return create_statement

    def display_data(self, where_clause={}):
        display_statement = 'SELECT '
        if len(where_clause) != 0:
            for column in self.columns:
                display_statement += column + ','
            display_statement = display_statement.rstrip(',') + ' '
            display_statement += 'FROM ' + self.table_name
            if len(where_clause.items()) != 0:
                display_statement += ' WHERE '
                for key, value in where_clause.items():
                    display_statement += key + '=\"' + value + '\" AND '
                display_statement = display_statement.rstrip(' AND ') + ";"
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
                    update_statement += key + '=\"' + value + '\" AND '
                update_statement = update_statement.rstrip(' AND ')
            update_statement += ' WHERE '
            for key, value in where_clause.items():
                update_statement += key + '=\"' + value + '\" AND '
            update_statement = update_statement.rstrip(' AND ') + ";"
        return update_statement

    def delete_data(self, where_clause={}):
        delete_statement = 'DELETE FROM ' + self.table_name + ' WHERE '
        for key, value in where_clause.items():
            delete_statement += key + '=\"' + value + '\" AND '
        delete_statement = delete_statement.rstrip(' AND ') + ";"
        return delete_statement

    def execute_statement(self, statement):
        self.c.execute(statement)
        rows = self.c.fetchall()
        return rows

    def disconnect_from_database(self):
        self.conn.close()
