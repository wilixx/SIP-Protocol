from packet import packet
from random import choice
from string import digits

class response(packet):
    __packet_ = None

    __provisional_responses = [(100, 'TRYING'), (180, 'RINGING'), (181, 'CALL IS BEING FORWARDED'), (182, 'QUEUED'), (183, 'SESSION PROGRESS'), (199, 'EARLY DIALOG TERMINATED')]
    __successful_responses = [(200, 'OK'), (202, 'ACCEPTED'), (204, 'NO NOTIFICATION')]
    __redirection_responses = [(300, 'MULTIPLE CHOICES'), (301, 'MOVED PERMANENTLY'), (302, 'MOVED TEMOPRARILY'), (305, 'USE PROXY'), (380, 'ALTERNATIVE SERIVICE')]
    __client_faliure_responses = [(400, 'BAD REQUEST'), (401, 'UNAUTHORIZED'), (402, 'PAYMENT REQUIRED'), (403, 'FORBIDDEN'), (404, 'NOT FOUND'), (405, 'METHOD NOT ALLOWED'), (406, 'NOT ACCEPTABLE'), (407, 'PROXY AUTHENTICATION REQUIRED'), (408, 'REQUEST TIMEOUT'), (409, 'CONFLICT'), (410, 'GONE'), (411, 'LENGTH REQUIRED'), (412, 'CONDITIONAL REQUEST FAILED'), (413, 'REQUEST ENTITY TOO LARGE'), (414, 'REQUEST-URI TOO LONG'), (415, 'UNSUPPORTED URI SCHEME'), (417, 'UKNOWN RESOURCE PRIORITY'), (420, 'BAD EXTENSION'), (421, 'EXTENSTION REQUIRED'), (422, 'SESSION INTERVAL TOO SMALL'), (423, 'INTERVAL TOO BRIEF'), (424, 'BAD LOCATION INFORMATION'), (428, 'USE IDENTITY HEADER'), (429, 'PROVIDE REFERRER IDENTITY'), (433, 'ANONIMITY DISALLOWED'), (436, 'BAD IDENTITY-INFO'), (437, 'UNSUPPORTED CERTIFICATE'), (438, 'INVALID IDENTITY HEADER'), (439, 'FIRST HOP LACKS OUTBOUND SUPPORT'), (440, 'MAX-BREADTH EXCEEDED'), (469, 'BAD INFO PACKAGE'), (470, 'CONSENT NEEDED'), (480, 'TEMPORARILY UNAVAILABLE'), (481, 'CALL/TRANSACTIONS DOES NOT EXIST'), (482, 'LOOP DETECTED'), (483, 'TOO MANY HOPS'), (484, 'ADDRESS INCOMPLETE'), (485, 'AMBIGUOUS'), (486, 'BUSY HERE'), (487, 'REQUEST TERMINATED'), (488, 'NOT ACCEPTABLE HERE'), (489, 'BAD EVENT'), (491, 'REQUEST PENDING'), (493, 'UNDECIPHERABLE'), (494, 'SECURITY AGREEMENT REQUIRED')]
    __server_faliure_responses = [(500, 'INTERNAL SERVER ERROR'), (501, 'NOT IMPLEMENTED'), (502, 'BAD GATEWAY'), (503, 'SERVICE UNAVAILABLE'), (504, 'SERVER TIME-OUT'), (505, 'VERSION NOT SUPPORTED'), (513, 'MESSAGE TO LARGE'), (580, 'PRECONDITIONED FALIURE')]
    __global_faliure_responses = [(600, 'BUSY EVERYWHERE'), (603, 'DECLINE'), (604, 'DOES NOT EXIST ANYWHERE'), (606, 'NOT ACCEPTABLE'), (607, 'UNWANTED')]
    __responses = [__provisional_responses, __successful_responses, __redirection_responses, __client_faliure_responses, __server_faliure_responses, __global_faliure_responses]

    def __init__(self):
        __packet_ = packet.packet()

    def __add_uri(self, code, status):
        self.__packet_ = 'SIP/2.0 ' + str(code) + ' ' + status
