# Remove sys.path because it does not work properly
from random import choice
from string import digits
from peer.server.server import server
from src import request_packet, response_packet
from src.database import database # Change directory to database_tests

class registerar(server):
    __s = None
    __db = None

    __server_name = ''
    __domain = ''
    __protocol = ''
    __port = 6050
    __server_network_name = ''
    __content_type = ''
    __content_sub_type = ''

    def __init__(self, server_name, domain, server_network_name, content_type, content_sub_type, protocol='TCP', port=6050):
        self.__initialize_db()
        self.__set_server_name(server_name)
        self.__set_domain(domain)
        self.__set_set_server_network_name(server_network_name)
        self.__set_content_type(content_type)
        self.__set_content_sub_type(content_sub_type)
        self.__set_protocol(protocol)
        self.__set_port(port)
        self.__s = server(6050)
        self.__s._create_server((self._register_server.__name__, self._register_server))

    def _register_server(self, client_socket):
        message = self.__s._receive_message(client_socket)
        if message[:8] == 'REGISTER':
            client_name = message.split('From')[1].split('<sip:')[1].split('@')[0]
            client_network_name = message.split('From')[1].split('<sip:')[0].split(' ')[1]
            seq_num = int(message.split('CSeq')[1].split(' ')[1]) + 1
            ip = client_socket.getsockname()[0]
            self.__db._execute_statement(self.__db._insert_data(client_name, client_network_name, '', ip))
            '''packet = self.ok(seq_num, client_name, client_network_name, 'REGISTER', 'REGISTER')
            client_socket.send(packet.encode('UTF-8'))
            print('')
            print('Sent OK Packet to complete client registeration')
            print('Registered client: ' + client_network_name)
            print('')
            self.establish_session(client_socket, seq_num, client_name, client_network_name)'''

    def _establish_session(self, client_socket, seq_num, client_name, client_network_name):
        invite_packet_a = self.__s._receive_message(client_socket)
        subject = invite_packet_a.split('Subject ')[1].split('\r\n')[0]
        update_statement = self.db.update_data({'client_name': client_name, 'client_network_name': client_network_name}, {'subject': subject})
        self.db.execute_statement(update_statement)
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
        r = request_packet.request_packet(1, self._server_name, self._domain, self._protocol, self._port, self._server_network_name, self._client_network_name, self._client_name, seq_num, 'INVITE', self._content_type, self._content_sub_type)
        packet = r.get_packet()
        return packet

    def _trying(self, seq_num, client_name, client_network_name, subject, request_type):
        r = response_packet.response_packet(100, self._server_name, self._domain, self._protocol, self._port, self._server_network_name, client_network_name, client_name, seq_num, request_type, subject, self._content_type, self._content_sub_type)
        packet = r.get_packet()
        return packet

    def _ringing(self, seq_num, client_name, client_network_name, subject, request_type):
        r = response_packet.response_packet(180, self._server_name, self._domain, self._protocol, self._port, self._server_network_name, client_network_name, client_name, seq_num, request_type, subject, self._content_type, self._content_sub_type)
        packet = r.get_packet()
        return packet

    def _ok(self, seq_num, client_name, client_network_name, subject, request_type):
        r = response_packet.response_packet(200, self.server_name, self.domain, self.protocol, self.port, self.server_network_name, client_network_name, client_name, seq_num, request_type, subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def __set_server_name(self, server_name):
        self.__server_name = server_name

    def __get_server_name(self):
        return self.__server_name

    def __set_domain(self, domain):
        self.__set_domain = domain

    def __get_domain(self):
        return self.__domain

    def __set_set_server_network_name(self, server_network_name):
        self.__server_network_name = server_network_name

    def __get_server_network_name(self):
        return self.__server_network_name

    def __set_content_type(self, content_type):
        self.__content_type = content_type

    def __get_content_type(self):
        return self.__content_type

    def __set_content_sub_type(self, content_sub_type):
        self.content_sub_type = content_sub_type

    def __get_content_sub_type(self):
        return self.__content_sub_type

    def __set_protocol(self, protocol):
        self.__protocol = protocol

    def __get_protocol(self):
        return self.__protocol

    def __set_port(self, port):
        self.__port = port

    def __get_port(self):
        return self.__port

    def __initialize_db(self):
        self.__db = database()  #Might have to add database_tests name