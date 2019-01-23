import sqlite3

conn = sqlite3.connect('clients.db')

c = conn.cursor()

table_name = 'clients'  #Get table name at run time, can also put in a fixed value
columns = [ 'client_name', 'client_network_name', 'subject' ]

def create_table():
    create_statement = 'CREATE TABLE ' + table_name + ' ('
    for column in columns:
        create_statement += column + ','
        create_statement += ')'

def display_data():
    display_statement = 'SELECT '
    for column in columns:
        display_statement += column + ','
    display_statement += 'FROM ' + table_name

def insert_data(client_name, client_network_name):
    insert_statement = 'INSERT INTO ' + table_name + ' VALUES(' + client_name + ',' + client_network_name + ')'

def delete_data(client_name):
    delete_statement = 'DELETE FROM ' + table_name + ' WHERE ' + client_name
