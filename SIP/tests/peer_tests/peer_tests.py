import unittest
from SIP.src.peer import peer

class testPeer(unittest.TestCase):
    
    def testConstructor():
        # Without parameters
        peer_ = peer()
        # With 1 parameters
        peer_ = peer('TCP')
        # With 2 parameters
        peer_ = peer('TCP', 6050)
        # With UDP
        peer_ = peer('UDP', 6050)