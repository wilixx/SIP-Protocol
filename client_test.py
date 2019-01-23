import client

client_name = 'CLIENT1'
domain = 'there.com'
protocol = 'TCP'
client_network_name = 'client1'
server_network_name = 'registerar'
server_name = 'REGISTERAR'
cseq_num = 1
request_type = [ 'INVITE', 'ACK', 'BYE' ]
subject = 'Happy Christmas'
content_type = 'application'
content_sub_type = 'sdp'
port = 6050

#seq_num number of packets
def enter_client_details():
    client_name = raw_input('Enter Client Name: ')
    domain = raw_input('Enter Domain Name: ')
    protocol = raw_input('Enter Protocol Name(TCP/UDP): ')
    client_network_name = raw_input('Enter client Network Name: ')
    server_network_name = raw_input('Enter server Network Name: ')
    server_name = raw_input('Enter server Name: ')
    subject = raw_input('Enter Subject: ')
    port = raw_input('Enter Port: ')

c = client.client(client_name, domain, protocol, port, client_network_name, server_network_name, server_name, content_type, content_sub_type)
