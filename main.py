import socket

import registerar
import client
#import transfer_server
import transfer_client


c = transfer_client.transfer_client(socket.gethostname())
c.get_file('SampleAudio.mp3')

'''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_addr = (socket.gethostname(), 6050)
s.connect(client_addr)
s.close()'''


'''sender_name = 'UserA'
domain = 'there.com'
protocol = 'TCP'
sender_network_name = 'LittleGuy'
receiver_network_name = 'BigGuy'
receiver_name = 'UserB'
cseq_num = 1
request_type = [ 'INVITE', 'ACK', 'BYE' ]
subject = 'Happy Christmas'
content_type = 'application'
content_sub_type = 'sdp'
port = 6050

c = client.client(sender_name, domain, protocol, port, receiver_network_name, sender_network_name, receiver_name, subject, content_type, content_sub_type)
r = registerar.registerar(sender_name, domain, protocol, port, receiver_network_name, sender_network_name, receiver_name, request_type[0], subject, content_type, content_sub_type)
c.invite(1)
print(' ')
r.trying(1)
print(' ')
r.ringing(1)
print(' ')
r.ok(1)
print(' ')
c.ack(1)
print(' ')'''

'''a = request_packet.request_packet()
b = request_packet.request_packet()
c = request_packet.request_packet()
d = response_packet.response_packet()
e = response_packet.response_packet()
f = response_packet.response_packet()
g = response_packet.response_packet()
p = payload.payload()

r = registerar.registerar()

sender_name = 'UserA'
domain = 'there.com'
protocol = 'TCP'
sender_network_name = 'LittleGuy'
receiver_network_name = 'BigGuy'
receiver_name = 'UserB'
cseq_num = 1
subject = 'Happy Christmas'
content_type = 'application'
content_sub_type = 'sdp'
port = 6050'''

'''client_packet_types = [ 1, 2, 3 ]
server_packet_types = [ 100, 180, 200 ]
packets = [ client_packet_types[0], server_packet_types[0], server_packet_types[1], server_packet_types[2], client_packet_types[1], client_packet_types[2], server_packet_types[2] ]


print('')
a.make_packet(1, 'UserA', 'there.com', 'UDP', 6050, 'LittleGuy', 'BigGuy', 'UserB', 1, 'Happy Christmas', 'application', 'sdp')
print(a.get_packet())
print('')

print(packet_types[1])
print('')
d.make_packet(100, 'UserB', 'there.com', 'UDP', 6050, 'BigGuy', 'LittleGuy', 'UserA', 1, 'TRYING', 'Happy Christmas', 'application', 'sdp')
print(d.get_packet())
print('')


print(packet_types[2])
print('')
e.make_packet(180, 'UserB', 'there.com', 'UDP', 6050, 'BigGuy', 'LittleGuy', 'UserA', 1, 'RINGING', 'Happy Christmas', 'application', 'sdp')
print(e.get_packet())
print('')

print(packet_types[3])
print('')
f.make_packet(200, 'UserB', 'there.com', 'UDP', 6050, 'BigGuy', 'LittleGuy', 'UserA', 1, 'OK', 'Happy Christmas', 'application', 'sdp')
print(f.get_packet())
print('')

print(packet_types[4])
print('')
b.make_packet(4, 'UserA', 'there.com', 'UDP', 6050, 'LittleGuy', 'BigGuy', 'UserB', 1, 'Happy Christmas', 'application', 'sdp')
print(b.get_packet())
print('')

print('Transfer Media')

print(packet_types[5])
print('')
c.make_packet(2, 'UserA', 'there.com', 'UDP', 6050, 'LittleGuy', 'BigGuy', 'UserB', 1, 'Happy Christmas', 'application', 'sdp')
print(c.get_packet())
print('')

print(packet_types[6])
print('')
g.make_packet(200, 'UserB', 'there.com', 'UDP', 6050, 'BigGuy', 'LittleGuy', 'UserA', 1, 'OK', 'Happy Christmas', 'application', 'sdp')
print(f.get_packet())
print('')'''
