from string import digits
from random import choice

class payload:
    payload = ''

    def __init__(self, sender_name, domain, destination_client_ip, media_type):
        self.make_payload(sender_name, domain, destination_client_ip, media_type)

    def get_payload(self):
        return self.payload

    def set_v(self, v=0):
        self.payload = 'v=' + str(v)

    def set_o(self, sender_name, domain):
        random_string = ''.join(choice(digits) for _ in range(8)) + ' ' + ''.join(choice(digits) for _ in range(10))
        self.payload += '\r\no=' + sender_name + ' ' + random_string + ' IN IP4 ' + domain

    def set_s(self):
        self.payload += '\r\ns=Session SDP'

    def set_c(self,ip):
        self.payload += '\r\nc=IN IP4 ' + ip

    def set_t(self):
        self.payload += '\r\nt=0 0'

    def set_m(self, media_type):
        self.payload += '\r\nm=' + media_type + ' ' + ''.join(choice(digits) for _ in range(5)) + ' RTP/AVP 0'

    def set_a(self):
        self.payload += '\r\na=rtpmap:0 PCMU/8000'

    def make_payload(self, sender_name, domain, ip, media_type):
        self.set_v()
        self.set_o(sender_name, domain)
        self.set_s()
        self.set_c(ip)
        self.set_t()
        self.set_m(media_type)
        self.set_a()
