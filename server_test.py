import registerar

server_name = 'REGISTERAR'
domain = 'there.com'
protocol = 'TCP'
server_network_name = 'registerar'
cseq_num = 1
request_type = [ 'INVITE', 'ACK', 'BYE' ]
subject = 'Happy Christmas'
content_type = 'application'
content_sub_type = 'sdp'
port = 6050

def enter_client_details():
    server_name = raw_input('Enter Client Name: ')
    domain = raw_input('Enter Domain Name: ')
    protocol = raw_input('Enter Protocol Name(TCP/UDP): ')
    server_network_name = raw_input('Enter server Network Name: ')
    subject = raw_input('Enter Subject: ')
    port = raw_input('Enter Port: ')


r = registerar.registerar(server_name, domain, protocol, port, server_network_name, content_type, content_sub_type)
