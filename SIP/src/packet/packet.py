from random import choice
from string import digits


class packet:
    __packet = ''

    def __init__(self, sender_name, domain, protocol, port,
                 receiver_name, receiver_network_name,
                 seq_num, request_type, call_id, subject,
                 content_type, content_sub_type, from_tag, to_tag):
        self.__make_packet(sender_name, domain, protocol, port,
                           receiver_name, receiver_network_name,
                           seq_num, request_type, call_id, subject,
                           content_type, content_sub_type, from_tag, to_tag)

    def get_packet(self):
        return self.__packet

    def __add_via(self, protocol, domain, port):
        self.__packet += '\r\nVia: SIP/2.0/' + protocol + ' ' + domain + \
            ':' + port + ';'

    def __add_from(self, sender_name, domain, from_tag):
        self.__packet += '\r\nFrom: ' + '<sip:' + sender_name + \
                         '@' + domain + '>;tag=' + from_tag

    def __add_to(self, receiver_name, domain, to_tag):
        if to_tag == '':
            self.__packet += '\r\nTo: ' + '<sip:' + receiver_name + \
                             '@' + domain + '>'
        else:
            self.__packet += '\r\nTo: ' + '<sip:' + receiver_name + \
                             '@' + domain + '>;tag=' + to_tag

    def __add_cseq(self, seq, request_type):
        self.__packet += '\r\nCSeq: ' + seq + ' ' + request_type

    def __add_subject(self, subject):
        self.__packet += '\r\nSubject: ' + subject

    def __add_call_id(self, call_id=None):
        if call_id is None:
            random_string = ''.join(choice(digits) for _ in range(8))
            self.__packet += '\r\nCall-ID: ' + random_string
        else:
            self.__packet += '\r\nCall-ID: ' + call_id

    def __add_contact(self, receiver_network_name, receiver_name, domain):  # Fix Contact
        if receiver_network_name == '' and receiver_name == '':
            self.__packet += '\r\nContact: ' + receiver_network_name + \
                             '<sip:' + receiver_name + '@' + domain + '>'
        else:
            self.__packet += '\r\nContact: ' + receiver_network_name + \
                             '<sip:' + receiver_name + '@' + domain + '>'
        if receiver_name == '':
            self.__packet += '\r\nContact: ' + receiver_network_name + \
                             '<sip:' + domain + '>'

    def __add_content_type(self, content_type, content_sub_type):
        self.__packet += '\r\nContent-Type: ' + content_type + '/' + \
            content_sub_type

    def __add_content_length(self):
        self.__packet += '\r\nContent-Length: ' + str(len(self.__packet))

    def __add_expires(self):
        self.__packet += '\r\nExpires: 3600'

    def __make_packet(self, sender_name, domain, protocol,
                      port, receiver_name,
                      receiver_network_name, seq_num, request_type, call_id,
                      subject, content_type, content_sub_type, from_tag,
                      to_tag):
        self.__add_via(protocol, domain, port)
        self.__add_to(receiver_name, domain, to_tag)
        self.__add_from(sender_name, domain, from_tag)
        self.__add_call_id(call_id)
        self.__add_cseq(seq_num, request_type)
        self.__add_contact(receiver_network_name, receiver_name, domain)
        # self.__add_expires()
        self.__add_subject(subject)
        self.__add_content_type(content_type, content_sub_type)
        self.__add_content_length()
