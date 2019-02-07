from random import choice
from string import digits


class packet:
    __packet = ''

    def __init__(self, request_type, sender_name, domain, protocol, port,
                 sender_network_name, receiver_network_name, receiver_name,
                 seq_num, subject, content_type, content_sub_type, tag='123'):
        self.__make_packet(request_type, sender_name, domain, protocol, port,
                           sender_network_name, receiver_network_name,
                           receiver_name, seq_num, subject, content_type,
                           content_sub_type, tag)

    def get_packet(self):
        return self.__packet

    def __add_uri(self, uri):
        self.__packet = uri + self.__packet

    def __add_via(self, protocol, domain, port):
        self.__packet += '\r\nVia SIP/2.0/' + protocol + ' ' + domain + ':' + \
            port

    def __add_from(self, sender_name, sender_network_name, domain, tag):
        self.__packet += '\r\nFrom: ' + sender_network_name + \
            '<sip:' + sender_name + '@' + domain + '>;tag=' + tag

    def __add_to(self, receiver_name, receiver_network_name, domain, tag):
        self.__packet += '\r\nTo: ' + receiver_network_name + \
            '<sip:' + receiver_name + '@' + domain + '>;tag=' + tag

    def __add_cseq(self, seq, packet_type):
        self.__packet += '\r\nCSeq: ' + seq + ' ' + packet_type

    def __add_subject(self, subject):
        self.__packet += '\r\nSubject: ' + subject

    def __add_call_id(self):
        random_string = ''.join(choice(digits) for _ in range(8))
        self.__packet += '\r\nCallID: ' + random_string

    def __add_contact(self, receiver_network_name, receiver_name, domain):
        self.__packet += '\r\nContact: ' + receiver_network_name + \
            '<sip:' + receiver_name + '@' + domain + '>'

    def __add_content_type(self, content_type, content_sub_type):
        self.__packet += '\r\nContent-Type: ' + content_type + '/' + \
            content_sub_type

    def __make_packet(self, request_type, sender_name, sender_network_name,
                      domain, protocol, port, receiver_name,
                      receiver_network_name, seq_num, subject, content_type,
                      content_sub_type, tag):
        self.__add_via(protocol, domain, port)
        self.__add_from(sender_network_name, sender_name, domain, tag)
        self.__add_to(receiver_network_name, receiver_name, domain, tag)
        self.__add_call_id()
        self.__add_cseq(seq_num, request_type)
        self.__add_subject(subject)
        self.__add_contact(receiver_network_name, receiver_name, domain)
        self.__add_content_type(content_type, content_sub_type)
