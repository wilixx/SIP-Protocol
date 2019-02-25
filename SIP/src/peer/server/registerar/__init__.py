from registerar import registerar

server_name = 'SIP_Server'
domain = '192.168.1.218'
protocol = 'UDP'
port = '5060'
server_network_name = 'SIP_SERVER'
content_type = 'application'
content_sub_type = 'sdp'

registerar_ = registerar(server_name, domain, server_network_name,
                         content_type, content_sub_type, protocol,
                         port)
