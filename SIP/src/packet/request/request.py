from sys import path
path.append('C:\\Users\\r&dtrainee3\\SIP-Protocol\\SIP\\src\\packet')
from packet import packet


class request:
    __packet_ = None

    __requests = ['INVITE', 'BYE', 'REGISTER', 'ACK']

    def __init__(self, request_type, sender_name, sender_network_name, domain,
                 protocol, port, branch, receiver_name, receiver_network_name,
                 seq_num, call_id, subject, content_type, content_sub_type,
                 from_tag):
        self.__packet_ = packet(sender_name, sender_network_name,
                                domain, protocol, port, branch, receiver_name,
                                receiver_network_name, seq_num,
                                call_id, request_type, subject, content_type,
                                content_sub_type, from_tag, '')
        self.__add_uri(request_type, receiver_name, domain)

    def __add_uri(self, request_type, receiver_name, domain):
        self.__packet_ = request_type + ' sip:' + receiver_name + \
                         '@' + domain + ' SIP/2.0' + \
                         self.__packet_.get_packet()

    # def __add_authorization(self, username, password, ):
    # Can add authorization later on
    #    self.__packet_

    def get_packet(self):
        return self.__packet_
