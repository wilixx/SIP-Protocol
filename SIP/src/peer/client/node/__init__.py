from node import node

# Sample UDP Node
username = 'CLIENT'
password = '1234'
client_name = 'client'
domain = 'VaaanInfra.com'
client_network_name = 'client'
content_type = 'application'
content_sub_type = 'sdp'
protocol = 'UDP'
port = '5060'

server_name = 'SIP-Server'
server_network_name = 'SIP-SERVER'
server_addr = ('192.168.1.218', 5060)

node_ = node(username, password, client_name, domain, client_network_name,
             content_type, content_sub_type, protocol, port)
node_._register_client(server_name, server_network_name, server_addr)
node_._deregister_client(server_name, server_network_name, server_addr)  # If not sent client is not complete and should not send it attempt to connect to server