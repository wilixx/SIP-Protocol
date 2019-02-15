import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\peer')
from client import client

username = 'client1'
password = 'password'

client_name = 'client'
domain = 'there.com'
protocol = 'TCP'
port = '5060'
client_network_name = 'CLIENT'
content_type = 'application'
content_sub_type = 'sdp'

client_ = client(username, password, client_name, domain, protocol, port,
                 client_network_name, content_type, content_sub_type)
client_.__s.sendto('hello', ('169.254.6.205', 5060))
#client_.connect_to_server(('169.254.6.205', 5060))  # Obtain server IP???
#print('Registering client')
#client_.register_client()
#print('Deregistering client')
#client_.deregister_client()
#client_.disconnect_client()
