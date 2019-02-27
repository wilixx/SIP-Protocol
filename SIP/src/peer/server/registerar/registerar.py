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
        print(message)
        print('')
        headers = message.split('\r\n')
        code = '200'
        for header in headers:
            if header[:4] == 'From':
                sender_name = header.split('@')[0].split('<')[1].split(':')[1]
                sender_network_name = header.split(' ')[1].split('<')[0]
                from_tag = header.split(';tag=')[1]
            if header[:3] == 'Via':
                domain = header.split(' ')[2].split(';')[0].split(':')[0]
                protocol = header.split('/')[2].split(' ')[0]
                port = header.split(':')[2].split(';')[0]
                branch = header.split(';')[1] + ';'
                branch += header.split(';')[2].split('=')[0]
            if header[:2] == 'To':
                receiver_name = header.split('@')[0].split('<')[1].split(':')
                receiver_name = receiver_name[0]
                receiver_network_name = header.split(' ')[1].split('<')[0]
            if header[:7] == 'Call-ID':
                call_id = header.split(': ')[1]
            if header[:4] == 'CSeq':
                seq_num = header.split(' ')[1][:1]
                request_type = header.split(' ')[2]
            if header[:7] == 'Subject':
                subject = header.split(': ')[1]
            if header[:12] == 'Content-Type':
                content_type = header.split(': ')[1].split('/')[0]
                content_sub_type = header.split(': ')[1].split('/')[1]
            to_tag = '423gv2'
        response_ = self._ok(code, sender_name, sender_network_name, domain,
                             protocol, port, branch, receiver_name,
                             receiver_network_name, seq_num, request_type,
                             call_id, subject, content_type, content_sub_type,
                             from_tag, to_tag)
        address = ('192.168.1.240', 5060)
        print('')
        print('OK message')
        print(response_)
        self.__server_.send_message(response_, address)

    def _establish_session(self, client_socket, seq_num, client_name,
                           client_network_name):
        invite_packet_a = self.__s._receive_message(client_socket)
        subject = invite_packet_a.split('Subject ')[1].split('\r\n')[0]
        update_statement = self.db.update_data({'client_name': client_name, 'client_network_name': client_network_name}, {'subject': subject})
        self.db.execute_statement(update_statement)

    def __initialize_db(self):
        self.__db = database()  # Might have to add database_tests name

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

    # def _invite(self, seq_num):
    #     packet = r.get_packet()
    #    return packet

    # def _trying(self, seq_num, client_name, client_network_name, subject, request_type):
    #     packet = r.get_packet()
    #    return packet

    # def _ringing(self, seq_num, client_name, client_network_name, subject, request_type):
    #    packet = r.get_packet()
    #    return packet

    def _ok(self, code, sender_name, sender_network_name, domain, protocol,
            port, branch, receiver_name, receiver_network_name, seq_num,
            request_type, call_id, subject, content_type, content_sub_type,
            from_tag, to_tag):
        response_ = response(code, sender_name, sender_network_name,
                             domain, protocol, port, branch, receiver_name,
                             receiver_network_name, seq_num, request_type,
                             call_id, subject, content_type,
                             content_sub_type, from_tag, to_tag)
        response_ = response_.get_packet()
        return response_
