from random import choice
from string import digits
from threading import Thread
from SIP.src.peer.server.server import server
from SIP.src.packet.request.request import request
from SIP.src.packet.response.response import response
from SIP.src.database.database import database
from SIP.src.peer.client.client import client


class registerar:
    __server_ = None
    __db = None

    __clients = list()

    def __init__(self, server_name, domain, server_network_name, content_type,
                 content_sub_type, protocol='TCP', port='6050'):
        self.__server_ = server(server_name, domain, protocol,
                                port, server_network_name, content_type,
                                content_sub_type)
        if protocol == 'TCP':
            self.__server_.create_server(self.tcp_register_client)
        if protocol == 'UDP':
            self.__server_.create_server(self.udp_register_client)

    def __obtain_client_info(self, message):
        username = None
        password = None
        sender_name = None
        receiver_name = None
        receiver_network_name = None
        domain = None
        port = None
        content_type = None
        content_sub_type = None
        protocol = None
        subject = None
        seq_num = None
        request_type = None
        from_tag = None
        call_id = None
        headers = message.split('\r\n')
        for header in headers:
            if header[:4] == 'From':
                sender_name = header.split('@')[0].split('<')[1].split(':')[1]  # Fix here
                from_tag = header.split(';tag=')[1]
            if header[:3] == 'Via':
                domain = header.split(' ')[2].split(';')[0].split(':')[0]
                protocol = header.split('/')[2].split(' ')[0]
                port = header.split(':')[2].split(';')[0]
            if header[:2] == 'To':
                receiver_name = header.split('@')[0].split(':')[2]
            if header[:7] == 'Call-ID':
                call_id = header.split(': ')[1]
            if header[:4] == 'CSeq':
                seq_num = header.split(' ')[1][:1]
                request_type = header.split(' ')[2]
            if header[:7] == 'Subject':
                subject = header.split(': ')[1]
            if header[:13] == 'Authorization':
                username = header.split('username=')[1].split(';')[0]
                password = header.split('password=')[1]
            if header[:12] == 'Content-Type':
                content_type = header.split(': ')[1].split('/')[0]
                content_sub_type = header.split(': ')[1].split('/')[1]
            if header[:7] == 'Contact':
                receiver_network_name = header.split(':')[2].split('@')[0]
        client_info = {
            'sender_name': sender_name,
            'from_tag': from_tag,
            'domain': domain,
            'protocol': protocol,
            'port': port,
            'receiver_name': receiver_name,
            'call_id': call_id,
            'seq_num': seq_num,
            'request_type': request_type,
            'subject': subject,
            'username': username,
            'password': password,
            'content_type': content_type,
            'content_sub_type': content_sub_type,
            'receiver_network_name': receiver_network_name
        }
        return client_info

    def tcp_register_client(self, client_socket):
        message = self.__server_.receive_message(client_socket)
        print(message)
        if message[:8] == 'REGISTER':
            self.register_client(message, client_socket=client_socket)

    def udp_register_client(self):
        (message, client_address) = self.__server_.receive_message(None)
        print(message)
        if message[:8] == 'REGISTER':
            thread = Thread(target=self.register_client, args=(message, client_address))
            thread.start()
        else:
            print('Unable to register')

    def register_client(self, message, client_address=None, client_socket=None):
        if client_socket is None:
            self.__initialize_db()
            client_info = self.__obtain_client_info(message)
            records = self.__db.print_records({
                                                'username':
                                                    client_info.get('username'),
                                                'password':
                                                    client_info.get('password'),
                                                'sender_name':
                                                    client_info.
                                                        get('sender_name')
                                               })
            to_tag = '423gv2'
            if records:
                code = '200'
                ok_packet_ = self._ok(code, client_info.get('sender_name'),
                                      client_info.get('domain'),
                                      client_info.get('protocol'),
                                      client_info.get('port'),
                                      client_info.get('receiver_name'),
                                      client_info.get('receiver_network_name'),
                                      client_info.get('seq_num'),
                                      client_info.get('request_type'),
                                      client_info.get('call_id'),
                                      'OK',
                                      client_info.get('content_type'),
                                      client_info.get('content_sub_type'),
                                      client_info.get('from_tag'),
                                      to_tag)
                self.__server_.send_message(ok_packet_, client_address)
                client_exists = False  # Remove flag
                for client in self.__clients:
                    if client_info.get('username') in client:
                        client_exists = True
                if client_exists:
                    print('Client ' + client_info.get('username') + \
                          ' already registered')
                    return None
                else:
                    self.__clients.append((client_info.get('username'),
                                           client_info.get('sender_name'),
                                           client_address))
                    print('Client ' + client_info.get('username') + \
                          ' registered')
                (message, client_address) = self.__server_.receive_message(None)
                print(message)
                if message[:10] == 'DEREGISTER':
                    message = self.deregister_client(message)
                    if message[8:11] == '200':
                        ok_packet_ = message
                        self.__server_.send_message(ok_packet_,
                                                    client_address)
                        print('Client ' + client_info.get('username') + \
                              ' deregistered')
                    if message[8:11] == '401':
                        unauthorized_packet_ = message
                        self.__server_.send_message(unauthorized_packet_,
                                                    client_address)
                        print('Client ' + client_info.get('username') + \
                              ' unauthorized')
                if message[:6] == 'INVITE':
                    invite_ = message
                    self.establish_session(invite_, client_address=client_address)
            else:
                code = '401'
                to_tag = '423gv2'  # Generate to tag & sender tag becomes receiver's from tag
                client_info = self.obtain_client_info(message)
                unauthorized_packet_ = self._unauthorized(code, client_info.get('sender_name'),
                                                          client_info.get('domain'),
                                                          client_info.get('protocol'),
                                                          client_info.get('port'),
                                                          client_info.get('receiver_name'),
                                                          client_info.get('receiver_network_name'),
                                                          client_info.get('seq_num'),
                                                          client_info.get('request_type'),
                                                          client_info.get('call_id'),
                                                          'Unauthorized',
                                                          client_info.get('content_type'),
                                                          client_info.get('content_sub_type'),
                                                          client_info.get('from_tag'),
                                                          to_tag)
                self.__server_.send_message(unauthorized_packet_, client_address)
                print('Client ' + client_info.get('username') + \
                      ' unauthorized')
        else:
            self.__initialize_db()
            client_info = self.__obtain_client_info(message)
            records = self.__db.print_records({
                                               'username':
                                                   client_info.get('username'),
                                               'password':
                                                   client_info.get('password'),
                                               'sender_name':
                                                   client_info.
                                                       get('sender_name')
                                               })
            to_tag = '423gv2'  # Generate to tag
            if records:
                code = '200'  # Fix Contact
                ok_packet_ = self._ok(code, client_info.get('sender_name'),
                                      client_info.get('domain'),
                                      client_info.get('protocol'),
                                      client_info.get('port'),
                                      '',
                                      '',
                                      client_info.get('seq_num'),
                                      client_info.get('request_type'),
                                      client_info.get('call_id'),
                                      'OK',
                                      client_info.get('content_type'),
                                      client_info.get('content_sub_type'),
                                      client_info.get('from_tag'),
                                      to_tag)
                ok_packet_ = response.remove_header(ok_packet_, 'To')
                self.__server_.send_message(ok_packet_)
                client_exists = False  # Remove flag
                for client in self.__clients:
                    if client_info.get('username') in client:
                        client_exists = True
                    if client_exists:
                        print('Client ' + client_info.get('username') + \
                              ' already registered')
                        return None
                    else:
                        self.__clients.append((client_info.get('username'),
                                               client_info.get('sender_name'),
                                               client_socket))
                        print('Client ' + client_info.get('username') + \
                              ' registered')
                        message = self.__server_.receive_message(client_socket)
                        print(message)
                        if message[:10] == 'DEREGISTER':
                            message = self.deregister_client(message)
                            if message[8:11] == '200':
                                ok_packet_ = message
                                self.__server_.send_message(ok_packet_,
                                                            client_socket)
                                print('Client ' + client_info.get('username') + \
                                      ' deregistered')
                            if message[8:11] == '401':
                                unauthorized_packet_ = message
                                self.__server_.send_message(unauthorized_packet_,
                                                            client_socket)
                                print('Client ' + client_info.get('username') + \
                                      ' unauthorized')
                        else:
                            print('Establish session')
                            self.establish_session(client_info
                                                        .get('sender_name'),
                                                    client_info
                                                        .get('receiver_client'))
            else:
                code = '401'
                to_tag = '423gv2'  # Generate to tag & sender tag becomes receiver's from tag
                client_info = self.obtain_client_info(message)
                unauthorized_packet_ = self._unauthorized(code, client_info.get(
                                                            'sender_name'
                                                          ),
                                                          client_info.get(
                                                            'domain'
                                                          ),
                                                          client_info.get(
                                                            'protocol'
                                                          ),
                                                          client_info.get(
                                                            'port'
                                                          ),
                                                          client_info.get(
                                                            'receiver_name'
                                                          ),
                                                          client_info.get(
                                                            'receiver_network_name'
                                                          ),
                                                          client_info.get(
                                                            'seq_num'),
                                                          client_info.get(
                                                            'request_type'),
                                                          client_info.get(
                                                            'call_id'
                                                          ),
                                                          'Unauthorized',
                                                          client_info.get(
                                                            'content_type'
                                                          ),
                                                          client_info.get(
                                                            'content_sub_type'
                                                          ),
                                                          client_info.get(
                                                              'from_tag'
                                                          ),
                                                          to_tag)
                self.__server_.send_message(unauthorized_packet_, client_socket)
                print('Client ' + client_info.get('username') + \
                      ' unauthorized')

    def deregister_client(self, message):  # Requires a sender_name and a sender_network_name to deregister from client
        client_info = self.__obtain_client_info(message)
        to_tag = '423gv2' # Generate to tag
        client_exists = False
        for client in self.__clients:
            if client_info.get('sender_name') in client:
                client_exists = True
                self.__clients.remove(client)
        if client_exists:
            code = '200'
            ok_packet_ = self._ok(code, client_info.get('sender_name'),
                                  client_info.get('domain'),
                                  client_info.get('protocol'),
                                  client_info.get('port'),
                                  client_info.get('receiver_name'),
                                  client_info.get('receiver_network_name'),
                                  client_info.get('seq_num'),
                                  client_info.get('request_type'),
                                  client_info.get('call_id'),
                                  'OK',
                                  client_info.get('content_type'),
                                  client_info.get('content_sub_type'),
                                  client_info.get('from_tag'),
                                  to_tag)
            return ok_packet_
        else:
            code = '401'
            unauthorized_packet_ = self._unauthorized(code, client_info.
                                                      get('sender_name'),
                                                      client_info.
                                                      get('domain'),
                                                      client_info.
                                                      get('protocol'),
                                                      client_info.
                                                      get('port'),
                                                      client_info.
                                                      get('receiver_name'),
                                                      client_info.
                                                      get('receiver_network_name'),
                                                      client_info.
                                                      get('seq_num'),
                                                      client_info
                                                      .get('request_type'),
                                                      client_info.
                                                      get('call_id'),
                                                      'Unauthorized',
                                                       client_info.
                                                      get('content_type'),
                                                      client_info.
                                                      get('content_sub_type'),
                                                      client_info
                                                      .get('from_tag'),
                                                      to_tag)
            return unauthorized_packet_

    def establish_session(self, message, client_address=None, client_socket=None):
        invite_ = message
        (message, client_address) = self.__server_.receive_message(None)
        if message[:6] == 'TRYING':
            trying_ = message
            print(trying_)
        (message, client_address) = self.__server_.receive_message(None)
        if message[:7] == 'RINGING':
            ringing_ = message
            print(ringing_)
        (message, client_address) = self.__server_.receive_message(None)
        # ack_ = ack_()
        if message[:10] == 'DEREGISTER':
            deregister_ = message
            print(deregister_)
            message = self.deregister_client(deregister_)
            client_info = self.__obtain_client_info(message)
            if message[8:11] == '200':
                ok_packet_ = message
                self.__server_.send_message(ok_packet_,
                                            client_address)
                print('Client ' + client_info.get('username') + \
                      ' deregistered')
            if message[8:11] == '401':
                unauthorized_packet_ = message
                self.__server_.send_message(unauthorized_packet_,
                                            client_address)
                print('Client ' + client_info.get('username') + \
                      ' unauthorized')


    def get_clients(self):
        return self.__clients

    def __initialize_db(self):
        self.__db = database('client_data')  # Might have to add database_tests name

    def _invite(self, sender_name, domain, protocol, port, receiver_name,
                receiver_network_name, seq_num, call_id,
                subject, content_type, content_sub_type, from_tag, to_tag):
        request_ = request('INVITE', sender_name, domain, protocol, port,
                         receiver_name, receiver_network_name, seq_num,
                         call_id, subject, content_type, content_sub_type,
                         from_tag, to_tag)
        request_ = request_.get_packet()
        return request_

    def _trying(self, sender_name, domain, protocol, port, receiver_name,
                receiver_network_name, seq_num, call_id, subject, content_type,
                content_sub_type, from_tag, to_tag):
        request_ = request('TRYING', sender_name, domain, protocol, port,
                           receiver_name, receiver_network_name, seq_num,
                           call_id, subject, content_type, content_sub_type,
                           from_tag, to_tag)
        request_ = request_.get_packet()
        return request_

    def _ringing(self, sender_name, domain, protocol, port, receiver_name,
                receiver_network_name, seq_num, call_id, subject, content_type,
                content_sub_type, from_tag, to_tag):
        request_ = request('RINGING', sender_name, domain, protocol, port,
                           receiver_name, receiver_network_name, seq_num,
                           call_id, subject, content_type, content_sub_type,
                           from_tag, to_tag)
        request_ = request_.get_packet()
        return request_

    def _ok(self, code, sender_name, domain, protocol, port,
            receiver_name, receiver_network_name, seq_num,
            request_type, call_id, subject, content_type, content_sub_type,
            from_tag, to_tag):
        response_ = response(code, sender_name, domain,
                             protocol, port, receiver_name,
                             receiver_network_name, seq_num, request_type,
                             call_id, subject, content_type,
                             content_sub_type, from_tag, to_tag)
        response_ = response_.get_packet()
        return response_

    def _unauthorized(self, code, sender_name, domain, protocol, port,
                      receiver_name, receiver_network_name, seq_num, request_type,
                      call_id, subject, content_type, content_sub_type,
                      from_tag, to_tag):
        response_ = response(code, sender_name, domain,
                             protocol, port, receiver_name,
                             receiver_network_name, seq_num, request_type,
                             call_id, subject, content_type,
                             content_sub_type, from_tag, to_tag)
        response_ = response_.get_packet()
        return response_
