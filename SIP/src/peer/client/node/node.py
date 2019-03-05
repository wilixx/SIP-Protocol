from SIP.src.peer.client.client import client
from SIP.src.database.database import database
from SIP.src.packet.request.request import request


class node:

    __client_ = None
    __db = None

    def __init__(self, username, password, client_name, domain,
                 client_network_name, content_type,
                 content_sub_type, protocol='UDP', port='5060'):
        self.__client_ = client(username, password, client_name, domain,
                                protocol, port, client_network_name,
                                content_type, content_sub_type)
        # self.__initialize_db()

    def _register_client(self, server_name, server_network_name, server_addr):
        seq_num = '1'  # Random SEQ num
        call_id = '44asdvasdvasdvag435tqw454q34t'  # Random call id
        from_tag = 'asv3442'
        subject = 'register packet'
        protocol = self.__client_.get_protocol()
        if protocol == 'UDP':
            register_packet = self._register(self.__client_.get_client_name(),
                                             self.__client_.get_domain(),
                                             self.__client_.get_protocol(),
                                             self.__client_.get_port(),
                                             server_name, server_network_name,
                                             seq_num, call_id, subject,
                                             self.__client_.get_content_type(),
                                             self.__client_.get_content_sub_type(),
                                             from_tag)
            self.__client_.send_message(register_packet, server_addr)
            packet = self.__client_.receive_message(protocol)
            headers = packet.split('\r\n')
            for header in headers:
                if header[:3] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got registered')
                    self.__client_.send_message(ok_packet)
                if header[:3] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
                    self.__client_.send_message(unauthorized_packet)
        if protocol == 'TCP':
            register_packet = self._register(self.__client_.get_client_name(),
                                             self.__client_.get_domain(),
                                             self.__client_.get_protocol(),
                                             self.__client_.get_port(),
                                             server_name, server_network_name,
                                             seq_num, call_id, subject,
                                             self.__client_.get_content_type(),
                                             self.__client_.get_content_sub_type(),
                                             from_tag)
            self.__client_.send_message(register_packet)
            packet = self.__client_.receive_message(protocol)
            headers = packet.split('\r\n')
            for header in headers:
                if header[:3] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got registered')
                    self.__client_.send_message(ok_packet)
                if header[:3] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
                    self.__client_.send_message(unauthorized_packet)

    def _deregister_client(self, server_name, server_network_name, server_addr):
        seq_num = '1'  # Random SEQ num
        call_id = '44asdvasdvasdvag435tqw454q34t'  # Random call id
        from_tag = 'asv3442'
        subject = 'deregister packet'
        protocol = self.__client_.get_protocol()
        if protocol == 'UDP':
            deregister_packet = self._deregister(self.__client_.get_client_name(),
                                                 self.__client_.get_domain(),
                                                 self.__client_.get_protocol(),
                                                 self.__client_.get_port(),
                                                 server_name,
                                                 server_network_name,
                                                 seq_num, call_id, subject,
                                                 self.__client_.get_content_type(),
                                                 self.__client_.get_content_sub_type(),
                                                 from_tag)
            self.__client_.send_message(deregister_packet, server_addr)
            packet = self.__client_.receive_message(protocol)
            headers = packet.split('\r\n')
            for header in headers:
                if header[:3] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got deregistered')
                    self.__client_.send_message(ok_packet)
                if header[:3] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
                    self.__client_.send_message(unauthorized_packet)
            self.__client_.disconnect_from_server()
        if protocol == 'TCP':
            deregister_packet = self._deregister(self.__client_.get_client_name(),
                                               self.__client_.get_domain(),
                                               self.__client_.get_protocol(),
                                               self.__client_.get_port(),
                                               server_name, server_network_name,
                                               seq_num, call_id, subject,
                                               self.__client_.get_content_type(),
                                               self.__client_.get_content_sub_type(),
                                               from_tag)
            self.__client_.send_message(deregister_packet)
            packet = self.__client_.receive_message(protocol)
            headers = packet.split('\r\n')
            for header in headers:
                if header[:3] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got registered')
                    self.__client_.send_message(ok_packet)
                if header[:3] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
                    self.__client_.send_message(unauthorized_packet)
            self.__client_.disconnect_from_server()

    # def _establish_session(self):
        # self.__client_.

    def __initialize_db(self):
        self.__db = database('client_data')
        # Might have to add database_tests name

    def _register(self, client_name, domain, protocol, port, server_name,
                  server_network_name, seq_num, call_id, subject, content_type,
                  content_sub_type, from_tag):
        request_ = request('REGISTER', client_name, domain, protocol, port,
                          server_name, server_network_name, seq_num, call_id,
                          subject, content_type, content_sub_type, from_tag)
        request_.add_authorization(self.__client_.get_username(),
                                   self.__client_.get_password())
        request_ = request_.get_packet()
        return request_

    def _deregister(self, client_name, domain, protocol, port, server_name,
                    server_network_name, seq_num, call_id, subject,
                    content_type, content_sub_type, from_tag):
        request_ = request('DEREGISTER', client_name, domain, protocol, port,
                           server_name, server_network_name, seq_num, call_id,
                           subject, content_type, content_sub_type, from_tag)
        request_.add_authorization(self.__client_.get_username(),
                                   self.__client_.get_password())
        request_ = request_.get_packet()
        return request_