import unittest
import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\database\\')
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\misc')
from logger import logger
from database import database
from os.path import exists


class database_test(unittest.TestCase):

    def test_insert_client_records(self):
        logger.log_print('\n')
        table_name = 'client_data'
        columns = ['id', 'username', 'password']
        db = database(table_name)
        values = [1, 'user1', 'password1']
        records = db.insert_records(values)
        log = 'Records inserted successfully: \n'
        for i in range(0, 2):
            log += columns[i] + ': ' + values[i] + ', '
        log = log.rstrip(', ')
        logger.log_print(log)
        insert_success = []
        self.assertEqual(records, insert_success)

    def test_print_all_client_records(self):
        logger.log_print('\n')
        table_name = 'client_data'
        columns = ['id', 'username', 'password']
        db = database(table_name)
        records = db.print_records()
        log = 'All records printed successfully: \n'
        for record in records:
            for i in range(0, 2):
                log += columns[i] + ': ' + record[i] + '\n'
        log = log.rstrip('\n')
        logger.log_print(log)
        values = [(1, 'user1', 'password1')]
        self.assertEqual(records, values)

    def test_print_client_records(self):
        logger.log_print('\n')
        table_name = 'client_data'
        columns = ['id', 'username', 'password']
        db = database(table_name)
        records = db.print_records(columns)
        log = 'Records by columns printed successfully: \n'
        for record in records:
            for i in range(0, 2):
                log += columns[i] + ': ' + record[i] + '\n'
        log = log.rstrip('\n')
        logger.log_print(log)
        values = [(1, 'user1', 'password1')]
        self.assertEqual(records, values)

    def test_update_client_records(self):
        logger.log_print('\n')
        table_name = 'client_data'
        columns = ['id', 'username', 'password']
        db = database(table_name)
        current_values = {'username': 'user1', 'password': 'password1'}
        update_values = {'password': 'password'}
        records = db.update_records(current_values, update_values)
        log = 'Records updated successfully: \nCurrent values: \n'
        for key, value in current_values.items():
            log += key + ': ' + value + ', '
        log = log.rstrip(', ')
        log += '\nUpdated values: \n'
        for key, value in update_values.items():
            log += key + ': ' + value + ', '
        log = log.rstrip(', \n')
        update_success = []
        logger.log_print(log)
        self.assertEqual(records, update_success)

    def test_delete_client_records(self):
        logger.log_print('\n')
        table_name = 'client_data'
        columns = ['id', 'username', 'password']
        db = database(table_name)
        records = db.delete_records({'username': 'user1', 'password': 'password'})
        log = 'Records deleted successfully'
        logger.log_print(log)
        delete_success = []
        self.assertEqual(records, delete_success)

    '''def insert_transfer_records(self):
        logger.log_print('\n')
        table_name = 'transfer_records'
        columns = ['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer']
        db = database(table_name, columns)
        records = db.insert_records({'sender_name': 'server', 'receiver_name': 'client', 'sender_ip': '192.168.1.10', 'receiver_ip': '192.168.1.4', 'media_type': 'audio', 'media_name': 'abc.mp3', 'date_of_transfer': '', 'time_of_transfer']})
        print(records)
        self.assertEquals(test, sample)

    def print_all_transfer_records(self):
        logger.log_print('\n')
        table_name = 'transfer_records'
        columns = ['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer']
        db = database(table_name, columns)
        records = db.prints_records()
        log = 'All records printed successfully: \n'
        for record in records:
            for i in range(0, 2):
                log += columns[i] + ': ' + record[i] + '\n'
        log = log.rstrip('\n')
        logger.log_print(log)
        values = []
        self.assertEquals(records, values)

    def print_transfer_records(self):
        logger.log_print('\n')
        table_name = 'transfer_records'
        columns = ['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer']
        db = database(table_name, columns)
        records = db.prints_records()
        log = 'All records printed successfully: \n'
        for record in records:
            for i in range(0, 2):
                log += columns[i] + ': ' + record[i] + '\n'
        log = log.rstrip('\n')
        logger.log_print(log)
        values = []
        self.assertEquals(records, values)

    def update_transfer_records(self):
        db = database('transfer_records', ['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer'])
        records = db.update_records(['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer'])
        print(records)
        self.assertEquals(test, sample)

    def delete_transfer_records(self):
        db = database('transfer_records', ['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer'])
        records = db.transfer_records(['sender_name', 'receiver_name', 'sender_ip', 'receiver_ip', 'media_type', 'media_name', 'date_of_transfer', 'time_of_transfer'])
        print(records)
        self.assertEquals(test, sample)'''

if __name__ == '__main__':
    logger = logger('Datbase Test Logger', 'database_test.log')
    unittest.main()
