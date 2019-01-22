import socket
import threading

import response_packet

class registerar:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addr = ((socket.gethostname(), 6050))
    buff_size = 4096
    max_num_of_clients = 10

    sender_name = ''
    domain = ''
    protocol = ''
    port = 6050
    receiver_network_name = ''
    sender_network_name = ''
    receiver_name = ''
    request_type = ''
    subject = ''
    content_type = ''
    content_sub_type = ''

    def __init__(self, sender_name, domain, protocol, port, receiver_network_name, sender_network_name, receiver_name, request_type, subject, content_type, content_sub_type):
        self.sender_name = sender_name
        self.domain = domain
        self.protocol = protocol
        self.port = port
        self.receiver_network_name = receiver_network_name
        self.sender_network_name = sender_network_name
        self.receiver_name = receiver_name
        self.request_type = request_type
        self.subject = subject
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
                client_socket.close()
        except KeyboardInterrupt:
            print('Closed socket')
        finally:
            self.s.close()

    def serve_client(self, client_socket, addr):
        msg = client_socket.recv(self.buff_size)
        print(msg)

    def trying(self, seq_num):
        r = response_packet.response_packet(100, self.sender_name, self.domain, self.protocol, self.port, self.sender_network_name, self.receiver_network_name, self.receiver_name, seq_num, self.request_type ,self.subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def ringing(self, seq_num):
        r = response_packet.response_packet(180, self.sender_name, self.domain, self.protocol, self.port, self.sender_network_name, self.receiver_network_name, self.receiver_name, seq_num, self.request_type, self.subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def ok(self, seq_num):
        r = response_packet.response_packet(200, self.sender_name, self.domain, self.protocol, self.port, self.sender_network_name, self.receiver_network_name, self.receiver_name, seq_num, self.request_type, self.subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet
