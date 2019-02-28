# Sample TCP Client
'''from client import client

username = 'client'
password = 'password'

client_name = 'client'
domain = 'VaaanInfra.com'
protocol = 'TCP'
port = '5060'
client_network_name = 'CLIENT'
content_type = 'application'
content_sub_type = 'sdp'

print('Creating server')
client_ = client(username, password, client_name, domain, protocol, port,
                 client_network_name, content_type, content_sub_type)
server_address = ('192.168.1.218', 5060)
print('Connecting to server')
client_.connect_to_server(server_address)
print('Sending message to server')
client_.send_message('Test message')
print('Disconnecting to server')
client_.disconnect_from_server()'''

# Sample UDP Client
'''from client import client

username = 'client'
password = 'password'

client_name = 'client'
domain = 'VaaanInfra.com'
protocol = 'TCP'
port = '5060'
client_network_name = 'CLIENT'
content_type = 'application'
content_sub_type = 'sdp'

print('Creating server')
client_ = client(username, password, client_name, domain, protocol, port,
                 client_network_name, content_type, content_sub_type)

server_address = ('192.168.1.218', 5060)
print('Connecting to server')
client_.connect_to_server(server_address)

print('Sending message to server')
client_.send_message('Test message')

print('Disconnecting to server')
client_.disconnect_from_server()'''

from .client import client