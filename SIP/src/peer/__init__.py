# from peer import peer


'''# TCP Server
peer_ = peer()
print('Trying to bind socket')
peer_.socket_bind()
print('Trying to listen on bound socket')
peer_.socket_listen(1)
print('Accepting socket')
client_socket, client_addr = peer_.socket_accept()
print(client_socket)
print(client_addr)
print('Receiving message')
message = peer_.server_receive_message(client_socket)
print('Message: ' + message)
peer_.socket_close()

# TCP Client
peer_ = peer()
print('Connecting to client')
peer_.socket_connect(peer_._get_s_address())
print('Sending message')
peer_.client_send_message('Test message', 'TCP')
print('Message sent')
peer_.socket_close()

# UDP Server
peer_ = peer('UDP')
print('Trying to bind socket')
peer_.socket_bind()
print('Receiving message')
message = peer_.server_receive_message()
print('Message: ' + message)
peer_.socket_close()

# UDP Client
peer_ = peer('UDP')
print('Sending message')
peer_.client_send_message('Test message', 'UDP', peer_._get_s_address())
print('Message sent')
peer_.socket_close()'''
from .peer import peer