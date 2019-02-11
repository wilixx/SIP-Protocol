from server.server import server
from client import client


server_name = 'server'
domain = 'there.com'
protocol = 'TCP'
port = '6050'
server_network_name = 'SERVER'
content_type = 'application'
content_sub_type = 'sdp'

server_ = server(server_name, domain, port, server_network_name, content_type, content_sub_type)


def _register_server(abc):
    print(abc)


print(server_._create_server(_register_server))
