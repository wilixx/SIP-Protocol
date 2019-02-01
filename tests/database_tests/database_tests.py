import unittest
import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\database\\')
from database import database

from os.path import exists

class TestDatabase(unittest.TestCase):

    def test_create_table(self):
        db = database()
        db.create_database()
        if exists('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\database_tests\\clients.db'):
            pass
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()