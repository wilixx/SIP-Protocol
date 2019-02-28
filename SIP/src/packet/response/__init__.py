# Prints a sample request packet
'''from response import response


code = '200'
sender_name = 'CLIENT'
domain = 'VaaanInfra.com'
port = '5060'
protocol = 'UDP'
receiver_name = 'SIP-SERVER'
receiver_network_name = 'SIP-Server'
seq_num = '1'
request_type = 'REGISTER'
call_id = 'somerandomcallid'
subject = 'SUBJECT'
content_type = 'application'
content_sub_type = 'sdp'
from_tag = 'from_tag'
to_tag = 'to_tag'

response_ = response(code, sender_name, domain, port, protocol, receiver_name,
                     receiver_network_name, seq_num, request_type, call_id,
                     subject, content_type, content_sub_type, from_tag, to_tag)
print(response_.get_packet())'''
from .response import response
