from request.request import request
from response.response import response

# from packet import packet

code = ('INVITE')
sender_name = 'server1'
domain = 'there.com'
protocol = 'TCP'
port = '6050'
sender_network_name = 'SERVER1'
receiver_network_name = 'CLIENT1'
receiver_name = 'client1'
seq_num = '1'
subject = 'subject'
content_type = 'application'
content_sub_type = 'sdp'
tag = '123'

req = request(code, sender_name, sender_network_name, domain, protocol, port,
              receiver_name, receiver_network_name, seq_num, subject, 
              content_type, content_sub_type, tag)
print(req.get_request_packet())

code = '200'
request_type = 'INVITE'
sender_name = 'server1'
domain = 'there.com'
protocol = 'TCP'
port = '6050'
sender_network_name = 'SERVER1'
receiver_network_name = 'CLIENT1'
receiver_name = 'client1'
seq_num = '1'
subject = 'subject'
content_type = 'application'
content_sub_type = 'sdp'
tag = '123'

res = response(code, sender_name, sender_network_name, domain, protocol, port,
               receiver_name, receiver_network_name, seq_num, request_type,
               subject, content_type, content_sub_type, tag)
print(res.get_response_packet())
