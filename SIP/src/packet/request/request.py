from packet import packet

class request(packet):
    __packet_ = None

    __requests = ['INVITE', 'BYE', 'REGISTER', 'ACK']

    def __init__(self):
        self.__packet_ = packet.packet()

    def __add_uri(self, status, receiver_name, domain):
        self.__packet_ = status + '<sip:' + receiver_name + '@' + domain + ' SIP/2.0' + self.__packet

