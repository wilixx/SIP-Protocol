from registerar import registerar

# Sample UDP registerar
server_name = 'SIP_Server'
domain = 'VaaanInfra.com'
protocol = 'UDP'
port = '5060'
server_network_name = 'SIP_SERVER'
content_type = 'application'
content_sub_type = 'sdp'


registerar_ = registerar(server_name, domain, server_network_name,
                         content_type, content_sub_type, protocol,
                         port)
clients = registerar_.get_clients()
print(clients)