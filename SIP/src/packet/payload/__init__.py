import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\packet\\payload')
from payload import payload

version = '0'
sender_name = 'server1'
session_id = '0000776624 9563745610'
country_code = 'IN'
ip_type = 'IP4'
domain = 'there.com'
ip_address = '10.6.29.100'
media_type = 'audio'
protocol_id = '49712'
media_transfer_type = 'RTP/AVP'
protocol = 'rtpmap'
port = '0'
communication_port = 'PCMU'
transfer_port = '8000'
session_name = 'SESSION SDP'
payload_ = payload(version, sender_name, session_id, country_code,
                   ip_type, domain, ip_address, media_type, protocol_id,
                   media_transfer_type, protocol, port, communication_port,
                   transfer_port, session_name)
print(payload_.get_payload())
