from random import choice
from string import digits

class response_packet:
    provisional_responses = [ (100, 'TRYING'), (180, 'RINGING'), (181, 'CALL IS BEING FORWARDED'), (182, 'QUEUED'),
                             (183, 'SESSION PROGRESS'), (199, 'EARLY DIALOG TERMINATED') ]
    successful_responses = [ (200, 'OK'), (202, 'ACCEPTED'), (204, 'NO NOTIFICATION') ]
    redirection_responses = [ (300, 'MULTIPLE CHOICES'), (301, 'MOVED PERMANENTLY'), (302, 'MOVED TEMOPRARILY'),
                             (305, 'USE PROXY'), (380, 'ALTERNATIVE SERIVICE') ]
    client_faliure_responses = [ (400, 'BAD REQUEST'), (401, 'UNAUTHORIZED'), (402, 'PAYMENT REQUIRED'),
                                (403, 'FORBIDDEN'), (404, 'NOT FOUND'), (405, 'METHOD NOT ALLOWED'),
                                (406, 'NOT ACCEPTABLE'), (407, 'PROXY AUTHENTICATION REQUIRED'),
                                (408, 'REQUEST TIMEOUT'), (409, 'CONFLICT'), (410, 'GONE'), (411, 'LENGTH REQUIRED'),
                                (412, 'CONDITIONAL REQUEST FAILED'), (413, 'REQUEST ENTITY TOO LARGE'),
                                (414, 'REQUEST-URI TOO LONG'), (415, 'UNSUPPORTED URI SCHEME'),
                                (417, 'UKNOWN RESOURCE PRIORITY'), (420, 'BAD EXTENSION'), (421, 'EXTENSTION REQUIRED'),
                                (422, 'SESSION INTERVAL TOO SMALL'), (423, 'INTERVAL TOO BRIEF'),
                                (424, 'BAD LOCATION INFORMATION'), (428, 'USE IDENTITY HEADER'),
                                (429, 'PROVIDE REFERRER IDENTITY'), (433, 'ANONIMITY DISALLOWED'),
                                (436, 'BAD IDENTITY-INFO'), (437, 'UNSUPPORTED CERTIFICATE'),
                                (438, 'INVALID IDENTITY HEADER'), (439, 'FIRST HOP LACKS OUTBOUND SUPPORT'),
                                (440, 'MAX-BREADTH EXCEEDED'), (469, 'BAD INFO PACKAGE'), (470, 'CONSENT NEEDED'),
                                (480, 'TEMPORARILY UNAVAILABLE'), (481, 'CALL/TRANSACTIONS DOES NOT EXIST'),
                                (482, 'LOOP DETECTED'), (483, 'TOO MANY HOPS'), (484, 'ADDRESS INCOMPLETE'),
                                (485, 'AMBIGUOUS'), (486, 'BUSY HERE'), (487, 'REQUEST TERMINATED'),
                                (488, 'NOT ACCEPTABLE HERE'), (489, 'BAD EVENT'), (491, 'REQUEST PENDING'),
                                (493, 'UNDECIPHERABLE'), (494, 'SECURITY AGREEMENT REQUIRED') ]
    server_faliure_responses = [ (500, 'INTERNAL SERVER ERROR'), (501, 'NOT IMPLEMENTED'), (502, 'BAD GATEWAY'),
                                (503, 'SERVICE UNAVAILABLE'), (504, 'SERVER TIME-OUT'), (505, 'VERSION NOT SUPPORTED'),
                                (513, 'MESSAGE TO LARGE'), (580, 'PRECONDITIONED FALIURE') ]
    global_faliure_responses = [ (600, 'BUSY EVERYWHERE'), (603, 'DECLINE'), (604, 'DOES NOT EXIST ANYWHERE'),
                                (606, 'NOT ACCEPTABLE'), (607, 'UNWANTED') ]
    responses = [ provisional_responses, successful_responses, redirection_responses, client_faliure_responses, server_faliure_responses, global_faliure_responses ]
    packet = ''

    def __init__(self, response_code, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, seq_num, subject, content_type, content_sub_type, tag='123'):
        self.make_packet(response_code, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, seq_num, subject, content_type, content_sub_type, tag)

    def get_packet(self):
        return self.packet

    def clear_packet(self):
        self.packet = ''

    def add_response_uri(self, response_code):
        self.packet += 'SIP/2.0 '
        if int(response_code/100) == 1:
            response = self.responses[0]
        if int(response_code/100) == 2:
            response = self.responses[1]
        if int(response_code/100) == 3:
            response = self.responses[2]
        if int(response_code/100) == 4:
            response = self.responses[3]
        if int(response_code/100) == 5:
            response = self.responses[4]
        if int(response_code/100) == 6:
            response = self.responses[5]
        for res in response:
            if res[0] == response_code:
                response = res
                break
        self.packet += str(response[0]) + ' ' + str(response[1])

    def add_via(self, protocol, domain, port):
        self.packet += '\r\nVia SIP/2.0/' + protocol + ' ' + domain + ':' + str(port)

    def add_from(self, sender_network_name, sender_name, domain, tag):
        self.packet += '\r\nFrom ' + sender_network_name + ' <sip:' + sender_name + '@' + domain + '>;tag=' + tag

    def add_to(self, receiver_network_name, receiver_name, domain, tag):
        self.packet += '\r\nTo ' + receiver_network_name + ' <sip:' + receiver_name + '@' + domain + '>;tag=' + tag

    def add_call_id(self):
        random_string = ''.join(choice(digits) for _ in range(8))
        self.packet += '\r\nCallID ' + random_string

    def add_cseq(self, seq_num, request_type):
        self.packet += '\r\nCSeq ' + str(seq_num) + ' ' + request_type

    def add_subject(self, subject):
        self.packet += '\r\nSubject ' + subject

    def add_contact(self, receiver_network_name, receever_name, domain):
        self.packet += '\r\nContact ' + receiver_network_name + '<sip:' + receever_name + '@' + domain + '>'

    def add_content_type(self, content_type, content_sub_type):
        self.packet += '\r\nContent-Type ' + content_type + '/' + content_sub_type

    #def add_content_length(self):   Find packet size

    def make_packet(self, response_code, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, seq_num, request_type, subject, content_type, content_sub_type, tag='123'):
        self.add_response_uri(response_code)
        self.add_via(protocol, domain, port)
        self.add_from(sender_network_name, sender_name, domain, tag)
        self.add_to(receiver_network_name, receiver_name, domain, tag)
        self.add_call_id()
        self.add_cseq(seq_num, request_type)
        self.add_subject(subject)
        self.add_contact(receiver_network_name, receiver_name, domain)
        self.add_content_type(content_type, content_sub_type)
