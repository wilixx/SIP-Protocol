from node import node

# Sample UDP Node
username = 'RAM'
password = 'pass'
client_name = 'ram'
domain = 'VaaanInfra.com'
client_network_name = 'Ram'
content_type = 'application'
content_sub_type = 'sdp'
protocol = 'UDP'
port = '5060'

server_name = 'SIP-Server'
server_network_name = 'SIP-SERVER'
server_addr = ('192.168.1.218', 5060)

node_ = node(username, password, client_name, domain, client_network_name,
             content_type, content_sub_type, protocol, port)
node_.register_client(server_name, server_network_name, server_addr)
node_.establish_session(server_name, server_network_name, server_addr)
node_.deregister_client(server_name, server_network_name, server_addr)  # If not sent client is not complete and should not send it attempt to connect to server