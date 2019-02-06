from sqlite3 import connect
from os.path import exists
import sys

class database:

    __table_name = None
    __columns = ['client_name', 'client_network_name', 'subject', 'ip']
    __conn = None
    __c = None

    __statement = ''

    def __init__(self, database_name='clients', table_name='clients', columns=None):
        db_file = database_name + '.db'
        if not exists(db_file):
            self.__create_database(db_file)
        self.__set_table_name(table_name)
        if columns != None:
            self.__set_columns(columns)
        self.__conn = connect(db_file)
        self.__c = self.__conn.cursor()
        print('Connected to database_tests')

    def __create_table(self):
        f = open(self.__database_name, 'r')
        f.close()

    def _create_table(self):
        create_statement = 'CREATE TABLE ' + self.__table_name + ' ('
        for column in self.__columns:
            create_statement += column + ' text,'
        create_statement = create_statement.rstrip(',')
        create_statement += ')' + ";"
        return create_statement