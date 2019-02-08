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
        packet = 'INVITE sip:client1@there.com SIP/2.0\r\nVia SIP/2.0/TCP there.com:6050\r\nFrom: server1<sip:SERVER1@there.com>;tag=123\r\nTo: CLIENT1<sip:client1@there.com>;tag=123\r\nCallID: 39626979\r\nCSeq: 1 INVITE\r\nSubject: subject\r\nContact: client1<sip:CLIENT1@there.com>\r\nContent-Type: application/sdp'
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
        packet = packet.split('CallID: ')[0] + 'CallID: ' + test_cseq + '\r\n' + packet.split('CallID: ')[1][10:]
        logger.log_print('\n' + 'Sample Request Packet: \r\n' + packet + '\n')
        logger.log_print('\n' + 'Test Response Packet: \r\n' + test_packet + '\n')
        self.assertEqual(request_.get_packet(), packet)

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
        packet = 'SIP/2.0 100 TRYING\r\nVia SIP/2.0/TCP there.com:6050\r\nFrom: server1<sip:SERVER1@there.com>;tag=123\r\nTo: CLIENT1<sip:client1@there.com>;tag=123\r\nCallID: 90815289\r\nCSeq: 1 INVITE\r\nSubject: subject\r\nContact: client1<sip:CLIENT1@there.com>\r\nContent-Type: application/sdp'
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
        packet = packet.split('CallID: ')[0] + 'CallID: ' + test_cseq + '\r\n' + packet.split('CallID: ')[1][10:]
        logger.log_print('\n' + 'Sample Response Packet: \r\n' + packet + '\n')
        logger.log_print('\n' + 'Test Response Packet: \r\n' + test_packet + '\n')
        self.assertEqual(test_packet, packet)

    def test_payload(self):
        payload_ = payload()

if __name__ == '__main__':
    logger.get_log_file_name('packet_test_log.log')
    unittest.main()
