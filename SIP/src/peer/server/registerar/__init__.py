from registerar import registerar

# Sample UDP registerar
server_name = 'Bob'
domain = 'VaaanInfra.com'
protocol = 'UDP'
port = '5060'
server_network_name = 'BOB'
content_type = 'application'
content_sub_type = 'sdp'

# Error in registerar

registerar_ = registerar(server_name, domain, server_network_name,
                         content_type, content_sub_type, protocol,
                         port)