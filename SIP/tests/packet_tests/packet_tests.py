import unittest
import sys
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\packet\\request')
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\packet\\response')
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\packet\\payload')
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\src\\packet')
sys.path.append('C:\\Users\\r&dtrainee3\\Desktop\\SIP-Protocol\\SIP\\misc')
import logger
from response import response
from request import request
from payload import payload


class packet_test(unittest.TestCase):
    def test_request_packet(self):
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
        sample_packet = 'INVITE sip:client1@there.com SIP/2.0\r\nVia SIP/2.0/TCP there.com:6050\r\nFrom: server1<sip:SERVER1@there.com>;tag=123\r\nTo: CLIENT1<sip:client1@there.com>;tag=123\r\nCallID: 39626979\r\nCSeq: 1 INVITE\r\nSubject: subject\r\nContact: client1<sip:CLIENT1@there.com>\r\nContent-Type: application/sdp'
        request_ = request(request_type, sender_name, sender_network_name,
                           domain, protocol, port, receiver_name,
                           receiver_network_name, seq_num,
                           subject, content_type, content_sub_type, tag)
        test_packet = request_.get_packet()
        test_cseq = test_packet.split('\r\n')
        for test in test_cseq:
            if 'CallID: ' in test:
                test_cseq = test.split(': ')
                test_cseq = test_cseq[1]
        sample_packet = sample_packet.split('CallID: ')[0] + 'CallID: ' + \
            test_cseq + '\r\n' + sample_packet.split('CallID: ')[1][10:]
        logger.log_print('\n' + 'Sample Request Packet: \r\n' + sample_packet + '\n')
        logger.log_print('\n' + 'Test Request Packet: \r\n' + test_packet + '\n')
        self.assertEqual(request_.get_packet(), sample_packet)

    def test_response_packet(self):
        code = '100'
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
        sample_packet = 'SIP/2.0 100 TRYING\r\nVia SIP/2.0/TCP there.com:6050\r\nFrom: server1<sip:SERVER1@there.com>;tag=123\r\nTo: CLIENT1<sip:client1@there.com>;tag=123\r\nCallID: 90815289\r\nCSeq: 1 INVITE\r\nSubject: subject\r\nContact: client1<sip:CLIENT1@there.com>\r\nContent-Type: application/sdp'
        response_ = response(code, sender_name, sender_network_name, domain,
                             protocol, port, receiver_name,
                             receiver_network_name, seq_num, request_type,
                             subject, content_type, content_sub_type, tag)
        test_packet = response_.get_packet()
        test_cseq = test_packet.split('\r\n')
        for test in test_cseq:
            if 'CallID: ' in test:
                test_cseq = test.split(': ')
                test_cseq = test_cseq[1]
        sample_packet = sample_packet.split('CallID: ')[0] + 'CallID: ' + \
            test_cseq + '\r\n' + sample_packet.split('CallID: ')[1][10:]
        logger.log_print('\n' + 'Sample Response Packet: \r\n' + sample_packet + '\n')
        logger.log_print('\n' + 'Test Response Packet: \r\n' + test_packet + '\n')
        self.assertEqual(test_packet, sample_packet)

    def test_payload(self):
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
        sample_payload = 'v=0\r\no=server1 0000776624 9563745610 IN IP4 there.com\r\ns=SESSION SDP\r\nt=0 0\r\nc=IN IP4 10.6.29.100\r\nm=audio 49712 RTP/AVP\r\na=rtpmap:0 PCMU/8000'
        test_payload = payload(version, sender_name, session_id, country_code,
                               ip_type, domain, ip_address, media_type,
                               protocol_id, media_transfer_type, protocol,
                               port, communication_port, transfer_port,
                               session_name)
        test_payload = test_payload.get_payload()
        logger.log_print('\n' + 'Sample Payload: \r\n' + sample_payload + '\n')
        logger.log_print('\n' + 'Test Payload: \r\n' + test_payload + '\n')
        self.assertEqual(sample_payload, test_payload)

if __name__ == '__main__':
    logger.get_log_file_name('packet_test_log.log')
    unittest.main()
