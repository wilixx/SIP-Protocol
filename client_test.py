import client

sender_name = 'UserA'
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
'''c.invite(1)
print(' ')
c.ack(1)
print(' ')'''
