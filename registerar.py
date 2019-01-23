import socket
import threading

import response_packet

class registerar:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_addr = ((socket.gethostname(), 6050))
    buff_size = 4096
    max_num_of_clients = 10

    server_name = ''
    domain = ''
    protocol = ''
    port = 6050
    server_network_name = ''
    content_type = ''
    content_sub_type = ''

    def __init__(self, server_name, domain, protocol, port, server_network_name, content_type, content_sub_type):
        self.server_name = server_name
        self.domain = domain
        self.protocol = protocol
        self.port = port
        self.server_network_name = server_network_name
        self.content_type = content_type
        self.content_sub_type = content_sub_type
        self.create_server(self.server_addr, self.max_num_of_clients)

    def create_server(self, server_addr, max_num_of_clients):
        self.s.bind(server_addr)
        print('Started SIP registerar server at: ' + str(self.server_addr))
        self.s.listen(max_num_of_clients)
        try:
            while True:
                (client_socket, addr) = self.s.accept()
                threading.Thread(self.serve_client(client_socket, addr)).run()
        except KeyboardInterrupt:
            print('Closed socket')
        finally:

            self.s.close()

    def serve_client(self, client_socket, addr):
        msg = client_socket.recv(self.buff_size).decode('UTF-8')
        print(msg)
        print('')
        if msg[:8] == 'REGISTER':
            client_name = msg.split('From')[1].split('<sip:')[1].split('@')[0]
            client_network_name = msg.split('From')[1].split('<sip:')[0].split(' ')[1]
            seq_num = int(msg.split('CSeq')[1].split(' ')[1]) + 1
            packet = self.ok(seq_num, client_name, client_network_name, 'REGISTER', 'REGISTER')
            client_socket.send(packet.encode('UTF-8'))
            # Save client details in database
            print('Registered client: ' + self.server_network_name)
            print('')
            #Establish session when we receive invite packet from client
            self.establish_session(client_socket, seq_num)

    def establish_session(self, client_socket, seq_num):
        #Get details of client from database
        client_name = 'CLIENT1'
        client_network_name = 'client1'
        subject = 'file name'
        invite_packet = client_socket.recv(self.buff_size)
        print(invite_packet.decode('UTF-8'))
        print('')
        trying_packet = self.trying(seq_num, client_name, client_network_name, subject, 'TRYING')
        client_socket.send(trying_packet.encode('UTF-8'))
        print('Sent trying packet')
        ringing_packet = self.ringing(seq_num, client_name, client_network_name, subject, 'RINGING')
        client_socket.send(ringing_packet.encode('UTF-8'))
        print('Sent ringing packet')
        ok_packet = self.ok(seq_num, client_name, client_network_name, subject, 'OK')
        client_socket.send(ok_packet.encode('UTF-8'))
        print('Sent ok packet')
        ack_packet = client_socket.recv(self.buff_size)
        print(ack_packet.decode('UTF-8'))
        print('')

    def trying(self, seq_num, client_name, client_network_name, subject, request_type):
        r = response_packet.response_packet(100, self.server_name, self.domain, self.protocol, self.port, self.server_network_name, client_network_name, client_name, seq_num, request_type, subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def ringing(self, seq_num, client_name, client_network_name, subject, request_type):
        r = response_packet.response_packet(180, self.server_name, self.domain, self.protocol, self.port, self.server_network_name, client_network_name, client_name, seq_num, request_type, subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def ok(self, seq_num, client_name, client_network_name, subject, request_type):
        r = response_packet.response_packet(200, self.server_name, self.domain, self.protocol, self.port, self.server_network_name, client_network_name, client_name, seq_num, request_type, subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet
