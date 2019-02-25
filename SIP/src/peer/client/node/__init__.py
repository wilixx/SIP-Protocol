from node import node

username = 'client_username'
password = 'client_password'
client_name = 'client'
domain = '192.168.1.218'
client_network_name = 'CLIENT'
rinstance = 'adsfbsfb345324'
content_type = 'application'
content_sub_type = 'sdp'

server_name = 'SIP-Server'
server_network_name = 'SIP-SERVER'
server_addr = (domain, 5060)

node_ = node(username, password, client_name, domain, client_network_name,
             rinstance, content_type, content_sub_type)
node_._register_client(server_name, server_network_name, server_addr)
