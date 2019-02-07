from packet import packet
from random import choice
from string import digits


class response(packet):
    __packet_ = None

    __provisional_responses = {'EARLY DIALOG TERMINATED': '199',
                               'CALL IS BEING FORWARDED': '181',
                               'RINGING': '180', 'QUEUED': '182',
                               'TRYING': '100', 'SESSION PROGRESS': '183'}
    __successful_responses = {'NO NOTIFICATION': '204', 'ACCEPTED': '202',
                              'OK': '200'}
    __redirection_responses = {'MOVED PERMANENTLY': '301', 'USE PROXY': '305',
                               'MULTIPLE CHOICES': '300',
                               'MOVED TEMOPRARILY': '302',
                               'ALTERNATIVE SERIVICE': '380'}
    __client_faliure_responses = {'INVALID IDENTITY HEADER': '438',
                                  'LENGTH REQUIRED': '411',
                                  'REQUEST ENTITY TOO LARGE': '413',
                                  'SECURITY AGREEMENT REQUIRED': '494',
                                  'TEMPORARILY UNAVAILABLE': '480',
                                  'NOT FOUND': '404', 'UNAUTHORIZED': '401',
                                  'CONFLICT': '409', 'NOT ACCEPTABLE': '406',
                                  'CALL/TRANSACTIONS DOES NOT EXIST': '481',
                                  'SESSION INTERVAL TOO SMALL': '422',
                                  'REQUEST PENDING': '491',
                                  'UKNOWN RESOURCE PRIORITY': '417',
                                  'GONE': '410', 'EXTENSTION REQUIRED': '421',
                                  'BAD REQUEST': '400',
                                  'BAD LOCATION INFORMATION': '424',
                                  'CONSENT NEEDED': '470',
                                  'USE IDENTITY HEADER': '428',
                                  'PROVIDE REFERRER IDENTITY': '429',
                                  'NOT ACCEPTABLE HERE': '488',
                                  'UNSUPPORTED CERTIFICATE': '437',
                                  'LOOP DETECTED': '482',
                                  'ADDRESS INCOMPLETE': '484',
                                  'PROXY AUTHENTICATION REQUIRED': '407',
                                  'TOO MANY HOPS': '483',
                                  'BAD EXTENSION': '420',
                                  'BAD IDENTITY-INFO': '436',
                                  'REQUEST TERMINATED': '487',
                                  'UNDECIPHERABLE': '493', 'FORBIDDEN': '403',
                                  'INTERVAL TOO BRIEF': '423',
                                  'REQUEST TIMEOUT': '408',
                                  'MAX-BREADTH EXCEEDED': '440',
                                  'BUSY HERE': '486',
                                  'FIRST HOP LACKS OUTBOUND SUPPORT': '439',
                                  'UNSUPPORTED URI SCHEME': '415',
                                  'CONDITIONAL REQUEST FAILED': '412',
                                  'ANONIMITY DISALLOWED': '433',
                                  'AMBIGUOUS': '485',
                                  'PAYMENT REQUIRED': '402',
                                  'BAD INFO PACKAGE': '469',
                                  'BAD EVENT': '489',
                                  'METHOD NOT ALLOWED': '405',
                                  'REQUEST-URI TOO LONG': '414'}
    __server_faliure_responses = {'BAD GATEWAY': '502',
                                  'MESSAGE TO LARGE': '513',
                                  'NOT IMPLEMENTED': '501',
                                  'SERVICE UNAVAILABLE': '503',
                                  'PRECONDITIONED FALIURE': '580',
                                  'INTERNAL SERVER ERROR': '500',
                                  'VERSION NOT SUPPORTED': '505',
                                  'SERVER TIME-OUT': '504'}
    __global_faliure_responses = {'BUSY EVERYWHERE': '600',
                                  'NOT ACCEPTABLE': '606',
                                  'DECLINE': '603',
                                  'DOES NOT EXIST ANYWHERE': '604',
                                  'UNWANTED': '607'}
    __responses = [__provisional_responses, __successful_responses,
                   __redirection_responses, __client_faliure_responses,
                   __server_faliure_responses, __global_faliure_responses]

    def __init__(self, code, sender_name, sender_network_name, domain,
                 protocol, port, receiver_name, receiver_network_name, seq_num,
                 request_type, subject, content_type, content_sub_type, tag):
        self.__packet_ = packet(sender_name, sender_network_name, domain,
                                protocol, port, receiver_name,
                                receiver_network_name, seq_num,
                                request_type, subject, content_type,
                                content_sub_type, tag)
        self.__add_uri(code)

    def __add_uri(self, code):
        response_code = int(code)
        find_response = int(response_code/100) - 1
        res = self.__responses[find_response].get('OK')
        print(res)
        # response_type = self.__responses[find_response][response_code]
        response_code = code
        self.__packet_ = 'SIP/2.0 ' + response_code + ' ' + response_type + \
                         self.__packet_.get_packet()

    def get_packet(self):
        return self.__packet_.get_packet()
