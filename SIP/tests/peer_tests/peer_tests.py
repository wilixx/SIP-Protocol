import unittest
from src.peer import peer


class testPeer(unittest.TestCase):    
    def test_constructor(self):
        # Without parameters
        peer_ = peer()
        # With 1 parameters
        peer_ = peer('TCP')
        # With 2 parameters
        peer_ = peer('TCP', 6050)
        # With UDP
        peer_ = peer('UDP', 6050)

    def test_socket_bind(self):
        # Test socket bind with TCP
        peer_ = peer()
        server_addr = peer_.get_s_address()
        peer_._socket_bind(server_addr)
        # Test socket bind with UDP
        peer_ = peer('UDP', 6050)
        server_addr = peer_.get_s_address()
        peer_._socket_bind(server_addr)

    def test_socket_accept(self):
        # Test socket accept with TCP
        peer_ = peer()
        server_addr = peer_.get_s_address()
        peer_._socket_accept(server_addr)
        # Test socket accept with UDP
        peer_ = peer('UDP')
        server_addr = peer_.get_s_address()
        peer_._socket_accept(server_addr)

    def test_socket_connect(self):
        # Test socket connect with TCP
        peer_ = peer()
        client_addr = ('127.0.0.1', '60000')
        peer_._socket_connect(client_addr)
        # Test socket connect with UDP
        peer_ = peer('UDP')
        client_addr = ('127.0.0.1', '60000')
        peer_._socket_connect(client_addr)

    def test_socket_listen(self):
        # Test socket listen using TCP
        peer_ = peer()
        backlogs = 5
        peer_._socket_listen(backlogs)
        # Test socket listen using UDP
        peer_ = peer('UDP')
        backlogs = 5
        peer_._socket_listen(backlogs)

    def test_socket_accept(self):
        # Test socket accept using TCP
        peer_ = peer()
        (client_socket, addr) = peer_._socket_accept()
        # Test socket accept using UDP
        peer_ = peer('UDP')
        (client_socket, addr) = peer_._socket_accept()

    def test_socket_close(self):
        # Test socket accept using TCP
        peer_ = peer()
        peer_._socket_close()
        # Test socket accept using TCP
        peer_ = peer('UDP')
        peer_._socket_close()

    def test_server_send_message(self):
        # Test send message using TCP
        peer_ = peer()
        message = 'Message'
        peer_._server_send_message(message)
        # Test send message using UDP
        peer_ = peer('UDP')
        message = 'Message'
        peer_._server_send_message(message)

    def test_client_send_message(self):
        # Test send message using TCP
        peer_ = peer()
        message = 'Message'
        client_socket = None
        peer_.client_send_message(client_socket, message)
        # Test send message using UDP
        peer_ = peer()
        message = 'Message'
        client_socket = None
        client_send_message(client_socket, message)
