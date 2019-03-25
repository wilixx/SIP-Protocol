from node import node

# Sample UDP Node
username = 'CLIENT'
password = '1234'
client_name = 'client'
domain = 'VaaanInfra.com'
client_network_name = 'Ram'
content_type = 'application'
content_sub_type = 'sdp'
protocol = 'UDP'
port = '5060'

receiver_name = 'client'
receiver_network_name = 'Client'
server_addr = ('192.168.1.249', 5060)

node_ = node(username, password, client_name, domain, client_network_name,
             content_type, content_sub_type, protocol, port)
node_.register_client(receiver_name, receiver_network_name, server_addr)
node_.sender_establish_session(receiver_name, receiver_network_name, server_addr)
node_.deregister_client(receiver_name, receiver_network_name, server_addr)  # If not sent client is not complete and should not send it attempt to connect to server