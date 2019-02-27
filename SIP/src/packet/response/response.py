from packet import packet
from random import choice
from string import digits


class response:
    __packet_ = None

    __provisional_responses = {'100': 'TRYING', '182': 'QUEUED',
                               '180': 'RINGING',
                               '199': 'EARLY DIALOG TERMINATED',
                               '183': 'SESSION PROGRESS',
                               '181': 'CALL IS BEING FORWARDED'}
    __successful_responses = {'202': 'ACCEPTED', '200': 'OK',
                              '204': 'NO NOTIFICATION'}
    __redirection_responses = {'300': 'MULTIPLE CHOICES',
                               '302': 'MOVED TEMOPRARILY',
                               '380': 'ALTERNATIVE SERIVICE',
                               '301': 'MOVED PERMANENTLY', '305': 'USE PROXY'}
    __client_faliure_responses = {'412': 'CONDITIONAL REQUEST FAILED',
                                  '482': 'LOOP DETECTED', '400': 'BAD REQUEST',
                                  '408': 'REQUEST TIMEOUT',
                                  '406': 'NOT ACCEPTABLE',
                                  '405': 'METHOD NOT ALLOWED',
                                  '428': 'USE IDENTITY HEADER',
                                  '422': 'SESSION INTERVAL TOO SMALL',
                                  '420': 'BAD EXTENSION', '403': 'FORBIDDEN',
                                  '438': 'INVALID IDENTITY HEADER',
                                  '484': 'ADDRESS INCOMPLETE',
                                  '494': 'SECURITY AGREEMENT REQUIRED',
                                  '433': 'ANONIMITY DISALLOWED',
                                  '413': 'REQUEST ENTITY TOO LARGE',
                                  '436': 'BAD IDENTITY-INFO',
                                  '440': 'MAX-BREADTH EXCEEDED',
                                  '401': 'UNAUTHORIZED', '489': 'BAD EVENT',
                                  '421': 'EXTENSTION REQUIRED',
                                  '439': 'FIRST HOP LACKS OUTBOUND SUPPORT',
                                  '480': 'TEMPORARILY UNAVAILABLE',
                                  '491': 'REQUEST PENDING', '404': 'NOT FOUND',
                                  '423': 'INTERVAL TOO BRIEF',
                                  '429': 'PROVIDE REFERRER IDENTITY',
                                  '415': 'UNSUPPORTED URI SCHEME',
                                  '470': 'CONSENT NEEDED',
                                  '487': 'REQUEST TERMINATED',
                                  '410': 'GONE', '493': 'UNDECIPHERABLE',
                                  '485': 'AMBIGUOUS', '483': 'TOO MANY HOPS',
                                  '402': 'PAYMENT REQUIRED',
                                  '414': 'REQUEST-URI TOO LONG',
                                  '424': 'BAD LOCATION INFORMATION',
                                  '486': 'BUSY HERE',
                                  '488': 'NOT ACCEPTABLE HERE',
                                  '411': 'LENGTH REQUIRED', '409': 'CONFLICT',
                                  '481': 'CALL/TRANSACTIONS DOES NOT EXIST',
                                  '437': 'UNSUPPORTED CERTIFICATE',
                                  '469': 'BAD INFO PACKAGE',
                                  '417': 'UKNOWN RESOURCE PRIORITY',
                                  '407': 'PROXY AUTHENTICATION REQUIRED'}
    __server_faliure_responses = {'505': 'VERSION NOT SUPPORTED',
                                  '580': 'PRECONDITIONED FALIURE',
                                  '500': 'INTERNAL SERVER ERROR',
                                  '513': 'MESSAGE TO LARGE',
                                  '504': 'SERVER TIME-OUT',
                                  '503': 'SERVICE UNAVAILABLE',
                                  '501': 'NOT IMPLEMENTED',
                                  '502': 'BAD GATEWAY'}
    __global_faliure_responses = {'604': 'DOES NOT EXIST ANYWHERE',
                                  '607': 'UNWANTED',
                                  '606': 'NOT ACCEPTABLE',
                                  '600': 'BUSY EVERYWHERE', '603': 'DECLINE'}

    __responses = [__provisional_responses, __successful_responses,
                   __redirection_responses, __client_faliure_responses,
                   __server_faliure_responses, __global_faliure_responses]

    def __init__(self, code, sender_name, sender_network_name, domain,
                 protocol, port, branch, receiver_name, receiver_network_name,
                 seq_num, request_type, call_id, subject, content_type,
                 content_sub_type, from_tag, to_tag):
        self.__packet_ = packet.packet(sender_name, sender_network_name,
                                       domain, protocol, port, branch,
                                       receiver_name, receiver_network_name,
                                       seq_num, request_type, call_id, subject,
                                       content_type, content_sub_type,
                                       from_tag, to_tag)
        self.__add_uri(code)

    def __add_uri(self, code):
        response_code = int(code)
        find_response = int(response_code/100) - 1
        response_type = self.__responses[find_response][code]
        self.__packet_ = 'SIP/2.0 ' + code + ' ' + response_type + \
                         self.__packet_.get_packet()

    def get_packet(self):
        return self.__packet_
