from SIP.src.peer.client.client import client
from SIP.src.database.database import database
from SIP.src.packet.request.request import request
from SIP.src.packet.response.response import response


class node:

    __client_ = None
    __db = None

    def __init__(self, username, password, client_name, domain,
                 client_network_name, content_type,
                 content_sub_type, protocol='UDP', port='5060'):
        self.__client_ = client(username, password, client_name, domain,
                                protocol, port, client_network_name,
                                content_type, content_sub_type)
        self.__initialize_db()

    def register_client(self, receiver_name, receiver_network_name, server_addr):
        seq_num = '1'  # Random SEQ num
        call_id = '44asdvasdvasdvag435tqw454q34t'  # Random call id
        from_tag = 'asv3442'
        protocol = self.__client_.get_protocol()
        if protocol == 'UDP':
            register_packet = self._register(self.__client_.get_client_name(),
                                             self.__client_.get_domain(),
                                             self.__client_.get_protocol(),
                                             self.__client_.get_port(),
                                             receiver_name, receiver_network_name,
                                             seq_num, call_id, 'REGISTER',
                                             self.__client_.get_content_type(),
                                             self.__client_.get_content_sub_type(),
                                             from_tag)
            self.__client_.send_message(register_packet, server_addr)
            packet = self.__client_.receive_message(protocol)
            print(packet)
            headers = packet.split('\r\n')
            for header in headers:
                if header[8:11] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got registered')
                    # How to know whether the client has to send a message
                    '''message = self.__client_.receive_message(protocol)
                    if message == 'sender_name':
                        client_info = self.obtain_client_info(ok_packet)
                        self.establish_session(client_info.get('sender_name'),
                                               client_info.get('sender_network_name'),
                                               server_addr)'''
                if header[8:11] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
        if protocol == 'TCP':
            self.__client_.connect_to_server(server_addr)
            register_packet = self._register(self.__client_.get_client_name(),
                                             self.__client_.get_domain(),
                                             self.__client_.get_protocol(),
                                             self.__client_.get_port(),
                                             receiver_name, receiver_network_name,
                                             seq_num, call_id, 'REGISTER',
                                             self.__client_.get_content_type(),
                                             self.__client_.get_content_sub_type(),
                                             from_tag)
            self.__client_.send_message(register_packet)
            packet = self.__client_.receive_message()
            print(packet)
            headers = packet.split('\r\n')
            for header in headers:
                if header[8:11] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got registered')
                    message = self.__client_.receive_message()
                    print(message)
                    self.establish_session(message, receiver_name,
                                           receiver_network_name, server_addr)
                if header[8:11] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')

    def deregister_client(self, receiver_name, receiver_network_name, server_addr):
        seq_num = '1'  # Random SEQ num
        call_id = '44asdvasdvasdvag435tqw454q34t'  # Random call id
        from_tag = 'asv3442'
        protocol = self.__client_.get_protocol()
        if protocol == 'UDP':
            deregister_packet = self._deregister(self.__client_.get_client_name(),
                                                 self.__client_.get_domain(),
                                                 self.__client_.get_protocol(),
                                                 self.__client_.get_port(),
                                                 receiver_name,
                                                 receiver_network_name,
                                                 seq_num, call_id, 'DEREGISTER',
                                                 self.__client_.get_content_type(),
                                                 self.__client_.get_content_sub_type(),
                                                 from_tag)
            self.__client_.send_message(deregister_packet, server_addr)
            packet = self.__client_.receive_message(protocol)
            headers = packet.split('\r\n')
            for header in headers:
                if header[8:11] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got deregistered')
                if header[8:11] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
            self.__client_.disconnect_from_server()
        if protocol == 'TCP':
            deregister_packet = self._deregister(self.__client_.get_client_name(),
                                                 self.__client_.get_domain(),
                                                 self.__client_.get_protocol(),
                                                 self.__client_.get_port(),
                                                 receiver_name, receiver_network_name,
                                                 seq_num, call_id, 'DEREGISTER',
                                                 self.__client_.get_content_type(),
                                                 self.__client_.get_content_sub_type(),
                                                 from_tag)
            self.__client_.send_message(deregister_packet)
            packet = self.__client_.receive_message(protocol)
            headers = packet.split('\r\n')
            for header in headers:
                if header[8:11] == '200':
                    ok_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got registered')
                if header[8:11] == '401':
                    unauthorized_packet = packet
                    print('Client ' + self.__client_.get_username() + \
                          ' got Unauthorized')
            self.__client_.disconnect_from_server()

    def sender_establish_session(self, receiver_name, receiver_network_name, server_addr):
        seq_num = '1'  # Random SEQ num
        call_id = '44asdvasdvasdvag435tqw454q34t'  # Random call id
        from_tag = 'asv3442'
        subject = 'INVITE'
        protocol = self.__client_.get_protocol()
        if protocol == 'UDP':
            invite_ = self._invite(self.__client_.get_client_name(),
                                   self.__client_.get_domain(),
                                   self.__client_.get_protocol(),
                                   self.__client_.get_port(),
                                   receiver_name, receiver_network_name,
                                   seq_num, call_id, subject,
                                   self.__client_.get_content_type(),
                                   self.__client_.get_content_sub_type(),
                                   from_tag)
            self.__client_.send_message(invite_, server_addr)
            trying_ = self._trying(self.__client_.get_client_name(),
                                   self.__client_.get_domain(),
                                   self.__client_.get_protocol(),
                                   self.__client_.get_port(),
                                   receiver_name, receiver_network_name,
                                   seq_num, call_id, subject,
                                   self.__client_.get_content_type(),
                                   self.__client_.get_content_sub_type(),
                                   from_tag)
            self.__client_.send_message(trying_, server_addr)
            ringing_ = self._ringing(self.__client_.get_client_name(),
                                    self.__client_.get_domain(),
                                    self.__client_.get_protocol(),
                                    self.__client_.get_port(),
                                    receiver_name, receiver_network_name,
                                    seq_num, call_id, subject,
                                    self.__client_.get_content_type(),
                                    self.__client_.get_content_sub_type(),
                                    from_tag)
            self.__client_.send_message(ringing_, server_addr)
        if protocol == 'TCP':
            invite_packet = self._invite(self.__client.get_client_name(),
                                         self.__client_.get_domain(),
                                         self.__cleint_.get_protocol(),
                                         self.__cleint_.get_port(),
                                         receiver_name, receiver_network_name,
                                         seq_num, call_id, subject,
                                         self.__cleint_.get_content_type(),
                                         self.__cleint_.get_content_sub_type(),
                                         from_tag)
            self.__client_.send_message(invite_packet)
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

    def __initialize_db(self):
        self.__db = database('client_data')

    def _invite(self, client_name, domain, protocol, port, server_name,
                server_network_name, seq_num, call_id, subject, content_type,
                content_sub_type, from_tag):
        request_ = request('INVITE', client_name, domain, protocol, port,
                           server_name, server_network_name, seq_num, call_id,
                           subject, content_type, content_sub_type, from_tag)
        request_ = request_.get_packet()
        return request_

    def _trying(self, sender_name, domain, protocol, port,
            receiver_name, receiver_network_name, seq_num,
            call_id, subject, content_type, content_sub_type,
            from_tag):
        request_ = request('TRYING', sender_name, domain,
                             protocol, port, receiver_name,
                             receiver_network_name, seq_num,
                             call_id, subject, content_type,
                             content_sub_type, from_tag)
        request_ = request_.get_packet()
        return request_

    def _ringing(self, sender_name, domain, protocol, port,
            receiver_name, receiver_network_name, seq_num,
            call_id, subject, content_type, content_sub_type,
            from_tag):
        request_ = request('RINGING', sender_name, domain,
                             protocol, port, receiver_name,
                             receiver_network_name, seq_num,
                             call_id, subject, content_type,
                             content_sub_type, from_tag)
        request_ = request_.get_packet()
        return request_

    def _ok(self, sender_name, domain, protocol, port,
            receiver_name, receiver_network_name, seq_num,
            call_id, subject, content_type, content_sub_type,
            from_tag, to_tag):
        response_ = response('OK', sender_name, domain,
                             protocol, port, receiver_name,
                             receiver_network_name, seq_num, 'OK',
                             call_id, subject, content_type,
                             content_sub_type, from_tag, to_tag)
        response_ = response_.get_packet()
        return response_

    def _register(self, client_name, domain, protocol, port, server_name,
                  server_network_name, seq_num, call_id, subject, content_type,
                  content_sub_type, from_tag):
        request_ = request('REGISTER', client_name, domain, protocol, port,
                          server_name, server_network_name, seq_num, call_id,
                          subject, content_type, content_sub_type, from_tag)
        request_.add_authorization(self.__client_.get_username(),
                                   self.__client_.get_password())
        request_ = request_.get_packet()
        request.remove_header(request_, 'To')
        return request_

    def _deregister(self, client_name, domain, protocol, port, server_name,
                    server_network_name, seq_num, call_id, subject,
                    content_type, content_sub_type, from_tag):
        request_ = request('DEREGISTER', client_name, domain, protocol, port,
                           server_name, server_network_name, seq_num, call_id,
                           subject, content_type, content_sub_type, from_tag)
        request_ = request_.get_packet()
        return request_