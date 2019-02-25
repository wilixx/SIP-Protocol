import sys
sys.path.append('C:\\Users\\r&dtrainee3\\SIP-Protocol\\SIP\\src')
sys.path.append('C:\\Users\\r&dtrainee3\\SIP-Protocol\\SIP\\src\\packet\\response')
from random import choice
from string import digits
from peer.server.server import server
from packet.request import request
from packet.response.response import response
from database import database


class registerar(server):
    __server_ = None
    __db = None

    def __init__(self, server_name, domain, server_network_name, content_type,
                 content_sub_type, protocol='TCP', port='6050'):
        # self.__initialize_db()
        self.__server_ = server(server_name, domain, protocol,
                                port, server_network_name, content_type,
                                content_sub_type)
        self.__server_.create_server(self.register_server)
        self.__initialize_db()

    def register_server(self, client_socket=None):
        message = self.__server_.receive_message(None)
        print('')
        print('Register message: ')
        # print(message)
        headers = message.split('\n')
        code = '200'
        for header in headers:
            if header[:4] == 'From':
                sender_name = header.split('@')[1].split('>')[0]
                sender_network_name = header.split('@')[0].split(':')[2]
            if header[:3] == 'Via':
                domain = header.split(' ')[1].split(';')[0]
                protocol = header.split('/')[2].split(' ')[0]
                port = header.split(':')[2].split(';')[0]
            if header[:2] == 'To':
                receiver_name = header.split('@')[1].split('>')[0]
                receiver_network_name = header.split('@')[0].split(':')[2]

    #  Fix headers and assign values to variables


        print(sender_name)
        print(sender_network_name)
        print(domain)
        print(protocol)
        print(port)
        print(receiver_name)
        print(receiver_network_name)
        raise('Error')
        '''sender_name = headers[5].split('@')[1].split('>')[0]
        sender_network_name = headers[5].split('@')[0].split(':')[2]
        domain = headers[0].split(':')[1].split(' ')[0]
        protocol = headers[1].split(' ')[1].split('/')[2]
        port = headers[3].split(':')[3].split(';')[0]
        receiver_name = headers[4].split('@')[1].split('>')[0]
        receiver_network_name = headers[4].split('@')[0].split(':')[2]
        seq_num = headers[7].split(':')[1].split(' ')[1]
        call_id = headers[6].split(': ')[1]
        request_type = headers[7].split(':')[1].split(' ')[2].split('\'')[0]
        rinstance = headers[3].split('=')[1].split('>')[0]
        branch = headers[1].split(';')[1] + ';' + headers[1].split(';')[2]
        subject = 'OK'
        content_type = 'application'
        content_sub_type = 'sdp'
        from_tag = headers[5].split('=')[1]
        to_tag = '6676'
        response_ = response(code, sender_name, sender_network_name,
                             domain, protocol, port, rinstance, branch,
                             receiver_name, receiver_network_name, seq_num,
                             call_id, request_type, subject, content_type,
                             content_sub_type, from_tag, to_tag)
        response_ = response_.get_packet()
        address = ('192.168.1.240', int(port))
        print('OK message')
        print(response_)
        self.__server_.send_message(response_, address)'''

    def _establish_session(self, client_socket, seq_num, client_name, client_network_name):
        invite_packet_a = self.__s._receive_message(client_socket)
        subject = invite_packet_a.split('Subject ')[1].split('\r\n')[0]
        update_statement = self.db.update_data({'client_name': client_name, 'client_network_name': client_network_name}, {'subject': subject})
        self.db.execute_statement(update_statement)

    def __initialize_db(self):
        self.__db = database()  #Might have to add database_tests name

        # payload = client_socket.recv(self.buff_size).decode('UTF-8')
        # print(payload)
        # print('')
        # display_statement = self.db.display_data({'client_name': client_name})
        # self.db.execute_statement(display_statement)
        # invite_packet_b = self.invite(1)
        # print(invite_packet_b)

        # Server receives invite packet from client1
        # Server sends invite packet to client2

        # Server sends client2 request to receive file
        # Server receives trying packet from client1
        # Server sends client2 trying packet
        # Server receives ringing packet from client1
        # Server sends client2 ringing packet
        # Server receives ok packet from client1
        # Server sends client2 ok packet

        # Server receives ack packet from client1
        # Server sends ack packet to client2

        # Start file transfer_tests from client1 to client2

        # Client1 sends bye packet to server
        # Server sends bye packet to client2
        # Client1 sends ok packet to server
        # Server sends ok packet to client2

    def _invite(self, seq_num):
        request_packet_ = request_packet.request_packet(1, self._server_name, self._domain, self._protocol, self._port, self._server_network_name, self._client_network_name, self._client_name, seq_num, 'INVITE', self._content_type, self._content_sub_type)
        packet = r.get_packet()
        return packet

    def _trying(self, seq_num, client_name, client_network_name, subject, request_type):
        request_packet_ = response_packet.response_packet(100, self._server_name, self._domain, self._protocol, self._port, self._server_network_name, client_network_name, client_name, seq_num, request_type, subject, self._content_type, self._content_sub_type)
        packet = r.get_packet()
        return packet

    def _ringing(self, seq_num, client_name, client_network_name, subject, request_type):
        request_packet_ = response_packet.response_packet(180, self._server_name, self._domain, self._protocol, self._port, self._server_network_name, client_network_name, client_name, seq_num, request_type, subject, self._content_type, self._content_sub_type)
        packet = r.get_packet()
        return packet

    def _ok(self, seq_num, client_name, client_network_name, subject, request_type):
        request_packet_ = response_packet.response_packet(200, self.server_name, self.domain, self.protocol, self.port, self.server_network_name, client_network_name, client_name, seq_num, request_type, subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet