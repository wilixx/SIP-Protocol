from random import choice
from string import digits

class request_packet:
    requests = ['INVITE', 'BYE', 'REGISTER', 'ACK']

    packet = ''

    def __init__(self, request_type, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, seq_num, subject, content_type, content_sub_type, tag='123'):
        self.make_packet(request_type, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, seq_num, subject, content_type, content_sub_type, tag)

    def get_packet(self):
        return self.packet

    def clear_packet(self):
        self.packet = ''

    def add_request_uri(self, request_type, sender_name, domain):
        if request_type == 1:
            self.packet += self.requests[0]
        if request_type == 2:
            self.packet += self.requests[1]
        if request_type == 3:
            self.packet += self.requests[2]
        if request_type == 4:
            self.packet += self.requests[3]
        self.packet += ' sip:' + sender_name + '@' + domain + ' SIP/2.0'

    def add_via(self, protocol, domain, port):
        self.packet += '\r\nVia SIP/2.0/' + protocol + ' ' + domain + ':' + str(port)

    def add_from(self, sender_network_name, sender_name, domain, tag):
        self.packet += '\r\nFrom ' + sender_network_name + ' <sip:' + sender_name + '@' + domain + '>;tag=' + str(tag)

    def add_to(self, receiver_network_name, receiver_name, domain, tag):
        self.packet += '\r\nTo ' + receiver_network_name + ' <sip:' + receiver_name + '@' + domain + '>;tag=' + str(tag)

    def add_call_id(self):
        random_string = ''.join(choice(digits) for _ in range(8))
        self.packet += '\r\nCallID ' + random_string

    def add_cseq(self, seq_num, request_type):
        self.packet += '\r\nCSeq ' + str(seq_num) + ' '
        if request_type == 1:
            self.packet += self.requests[0]
        if request_type == 2:
            self.packet += self.requests[1]
        if request_type == 3:
            self.packet += self.requests[2]
        if request_type == 4:
            self.packet += self.requests[3]

    def add_subject(self, subject):
        self.packet += '\r\nSubject ' + subject

    def add_contact(self, receiver_network_name, receiver_name, domain):
        self.packet += '\r\nContact ' + receiver_network_name + ' <sip:' + receiver_name + '@' + domain + '>'

    def add_content_type(self, content_type, content_sub_type):
        self.packet += '\r\nContent-Type ' + content_type + '/' + content_sub_type

    #def add_content_length(self):   Find packet size

    def make_packet(self, request_type, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, seq_num, subject, content_type, content_sub_type, tag='123'):
        self.add_request_uri(request_type, sender_name, domain)
        self.add_via(protocol, domain, port)
        self.add_from(sender_network_name, sender_name, domain, tag)
        self.add_to(receiver_network_name, receiver_name, domain, tag)
        self.add_call_id()
        self.add_cseq(seq_num, request_type)
        self.add_subject(subject)
        self.add_contact(receiver_network_name, receiver_name, domain)
        self.add_content_type(content_type, content_sub_type)
