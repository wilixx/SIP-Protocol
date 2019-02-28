# Prints a sample packet
'''from packet import packet


sender_name = 'client'
domain = 'VaaanInfra.com'
protocol = 'UDP'
port = '5060'
receiver_name = 'SIP-Server'
receiver_network_name = 'SIP-SERVER'
seq_num = '1'
request_type = 'REGISTER'
call_id = 'randomcallid'
subject = 'SUBJECT'
content_type = 'application'
content_sub_type = 'sdp'
from_tag = 'from_tag'
to_tag = 'to_tag'

packet_ = packet(sender_name, domain, protocol, port, receiver_name, receiver_network_name, seq_num, request_type, call_id, subject, content_type, content_sub_type, from_tag, to_tag)
packet = packet_.get_packet()
print(packet)'''
from .packet import packet


