# Prints a sample request packet
'''from request import request


sender_name = 'CLIENT'
domain = 'VaaanInfra.com'
protocol = 'UDP'
port = '5060'
receiver_name = 'SIP-SERVER'
receiver_network_name = 'SIP-Server'
seq_num = '1'
request_type = 'REGISTER'
call_id = 'somerandomcallid'
subject = 'SUBJECT'
content_type = 'application'
content_sub_type = 'sdp'
from_tag = 'from_tag'

request_ = request(sender_name, domain, protocol, port, receiver_name, receiver_network_name, seq_num, request_type, call_id, subject, content_type, content_sub_type, from_tag)
request_ = request_.get_packet()
print(request_)'''
from .request import request