from SIP.src.packet.packet import packet


class request:
    __packet_ = None

    __requests = ['INVITE', 'BYE', 'REGISTER', 'ACK']

    def __init__(self, request_type, sender_name, domain, protocol,
                 port, receiver_name, receiver_network_name,
                 seq_num, call_id, subject, content_type, content_sub_type,
                 from_tag):
        self.__packet_ = packet(sender_name, domain, protocol,
                                port, receiver_name,
                                receiver_network_name, seq_num,
                                request_type, call_id, subject, content_type,  # SEQ num # Request_type
                                content_sub_type, from_tag, '')
        self.__add_uri(request_type, receiver_name, domain)

    def __add_uri(self, request_type, receiver_name, domain):
        self.__packet_ = request_type + ' sip:' + receiver_name + \
                         '@' + domain + ' SIP/2.0' + \
                         self.__packet_.get_packet()

    def add_authorization(self, username, password):
        headers = self.__packet_.split('\r\n')
        authorization_header = 'Authorization: username=' + username + \
                               ';password=' + password
        for header in headers:
            if header[:7] == 'Subject':
                subject_index = headers.index(header) + 1 # Check var name here
        headers.insert(subject_index, authorization_header)
        self.__packet_ = '\r\n'.join(headers)

    @staticmethod
    def remove_header(packet, header_name):
        headers = packet.split('\r\n')
        for header in headers:
            if header[:2] == header_name:
                headers.remove(header)
        packet = '\r\n'.join(headers)
        return packet

    def get_packet(self):
        return self.__packet_
