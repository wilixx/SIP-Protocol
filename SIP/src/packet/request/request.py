from packet import packet


class request(packet):
    __packet_ = None

    __requests = ['INVITE', 'BYE', 'REGISTER', 'ACK']

    def __init__(self, request_type, sender_name, sender_network_name, domain,
                 protocol, port, receiver_name, receiver_network_name, seq_num,
                 subject, content_type, content_sub_type, tag):
        self.__packet_ = packet(sender_name, sender_network_name,
                                domain, protocol, port, receiver_name,
                                receiver_network_name, seq_num, request_type,
                                subject, content_type, content_sub_type, tag)
        self.__add_uri(request_type, receiver_name, domain)

    def __add_uri(self, request_type, receiver_name, domain):
        self.__packet_ = request_type + ' sip:' + receiver_name + \
            '@' + domain + ' SIP/2.0' + self.__packet_.get_packet()

    def get_request_packet(self):
        return self.__packet_
