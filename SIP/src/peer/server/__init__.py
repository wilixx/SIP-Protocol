import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\peer')
from server import server

server_name = 'server'
domain = '192.168.1.218'
protocol = 'TCP'
port = '6050'
server_network_name = 'SERVER'
content_type = 'application'
content_sub_type = 'sdp'

server_ = server(server_name, domain, protocol, port, server_network_name,
                 content_type, content_sub_type)


#def register_server(client_socket):
   # message = client_socket.recv(4096)
  #  print(message)
  #  message = client_socket.recv(4096)
    #print(message)

server_.create_server()
