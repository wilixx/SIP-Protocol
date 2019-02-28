# Sample TCP Server
'''from server import server


server_name = 'server'
domain = '192.168.1.218'
protocol = 'TCP'
port = '5060'
server_network_name = 'SERVER'
content_type = 'application'
content_sub_type = 'sdp'

server_ = server(server_name, domain, protocol, port, server_network_name,
                 content_type, content_sub_type)

def register_server(client_socket):
    print('Registering server')
    message = server_.receive_message(client_socket)
    print(message)
    server_.send_message('Received message + ' + message)
    print('Message sent')

server_.create_server(register_server)'''

# Sample UDP Server
'''from server import server


server_name = 'server'
domain = 'VaaanInfra.com'
protocol = 'UDP'
port = '5060'
server_network_name = 'SERVER'
content_type = 'application'
content_sub_type = 'sdp'

server_ = server(server_name, domain, protocol, port, server_network_name,
                 content_type, content_sub_type)

def register_server():
    print('Registering server')
    message = server_.receive_message()
    print(message)
    address = ('192.168.1.218', 5060)
    server_.send_message(('Received message: ' + message), address)
    print('Message sent')

server_.create_server(register_server)'''

from .server import server
