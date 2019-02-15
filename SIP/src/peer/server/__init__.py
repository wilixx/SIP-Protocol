'''import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\peer')
from server import server

server_name = 'server'
domain = '192.168.1.218'
protocol = 'UDP'
port = '5060'
server_network_name = 'SERVER'
content_type = 'application'
content_sub_type = 'sdp'

server_ = server(server_name, domain, protocol, port, server_network_name,
                 content_type, content_sub_type)


def register_server(message):
    print(message)

server_.create_server(register_server)'''
