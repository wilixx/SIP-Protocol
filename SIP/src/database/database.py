from sqlite3 import connect
from sqlite3 import Error
from os.path import exists
import sys


class database:

    __tables = ['clients', 'transfer_records']
    __client_columns = ['username', 'password']
    __transfer_records_columns = ['sender_name', 'receiver_name', 'sender_ip',
                                  'receiver_ip', 'media_type', 'media_name',
                                  'date_of_transfer', 'time_of_transfer']
    __table_name = None
    __columns = None
    __conn = None
    __c = None

    __statement = ''

    def __init__(self, table_name, columns):
        db_file = 'clients.db'
        self.__conn = connect(db_file)
        self.__c = self.__conn.cursor()
        if not exists(db_file):
            self.__create_database(db_file)
        self.__set_table_name(table_name, columns)
        self.__set_columns(table_name, columns)
        self.__conn = connect(db_file)
        self.__c = self.__conn.cursor()
        print('Connected to database')

    def __create_database(file_name):
        file = open(file_name, 'w')
        file.close()

    def __set_table_name(self, table_name, columns):
        self.__statement = 'SELECT name from sqlite_master WHERE type=\"table\"'
        tables = self.__execute_query()
        if len(tables) > 0:
            if table_name in tables:
                self.__table_name = table_name
        else:
            self.__create_table(table_name, columns)
            self.__table_name = table_name

    def __set_columns(self, table_name, columns):
        get_columns_query = 'PRAGMA table_info(' + table_name + ')'
        self.__statement = get_columns_query
        rows = self.__execute_query()
        self.__columns = columns

    def __execute_query(self):
        try:
            self.__c.execute(self.__statement)
            rows = self.__c.fetchall()
            return rows
        except Error:
            print(Error)

    def __disconnect_from_server(self):
        self.__conn.close()

    def print_records(self, columns=None):
        print_statement = 'SELECT '
        if columns is None:
            print_statement += '* FROM ' + self.__table_name
        else:
            for column in columns:
                print_statement += column + ','
            print_statement = print_statement.rstrip(', ')
        self.__statement = print_statement

    def insert_records(self, values):
        insert_statement = 'INSERT INTO ' + self.__table_name + ' VALUES('
        for value in values:
            insert_statement += '\'' + value + '\','
        insert_statement = insert_statement.rstrip(',') + ')'
        self.__statement = insert_statement

    def update_records(self, current_values={}, update_values={}):
        update_statement = 'UPDATE ' + self.__table_name + ' SET '
        for key, value in update_values.items():
            update_statement += key + '=\'' + value + '\' AND '
        update_statement = update_statement.rstrip(' AND ') + ' WHERE '
        for key, value in current_values.items():
            update_statement += key + '=\'' + value + '\' AND '
        update_statement = update_statement.rstrip(' AND ')
        self.__statement = update_statement

    def delete_records(self, values={}):
        delete_statement = 'DELETE FROM ' + self.__table_name + ' WHERE '
        for key, value in values.items():
            delete_statement += key + '=\'' + value + '\' AND '
        delete_statement = delete_statement.rstrip(' AND ')
        self.__statement = delete_statement

    def __create_table(self, table_name, columns):
        create_statement = 'CREATE TABLE ' + table_name + ' ('
        for column in columns:
            create_statement += column + ' text,'
        create_statement = create_statement.rstrip(',')
        create_statement += ')' + ";"
        self.__statement = create_statement
