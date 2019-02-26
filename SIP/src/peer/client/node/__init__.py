from node import node

username = '8007'
password = '1234'
client_name = 'client'
domain = 'VaaanInfra.com'
client_network_name = 'CLIENT'
rinstance = 'adsfbsfb345324'
content_type = 'application'
content_sub_type = 'sdp'

server_name = 'SIP-Server'
server_network_name = 'SIP-SERVER'
server_addr = ('192.168.1.218', 5060)

node_ = node(username, password, client_name, domain, client_network_name,
             rinstance, content_type, content_sub_type)
node_._register_client(server_name, server_network_name, server_addr)
