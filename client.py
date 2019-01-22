import socket

import transfer_server
import transfer_client
import request_packet
import payload


class client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sender_name = ''
    domain = ''
    protocol = ''
    port = 6050
    sender_network_name = ''
    receiver_network_name = ''
    receiver_name = ''
    subject = ''
    content_type = ''
    content_sub_type = ''
    tag = 123

    client_addr = (socket.gethostname(), port)

    def __init__(self, sender_name, domain, protocol, port, sender_network_name, receiver_network_name, receiver_name, subject, content_type, content_sub_type):
        self.sender_name = sender_name
        self.domain = domain
        self.protocol = protocol
        self.port = port
        self.sender_network_name = sender_network_name
        self.receiver_network_name = receiver_network_name
        self.receiver_name = receiver_name
        self.subject = subject
        self.content_type = content_type
        self.content_sub_type = content_sub_type
        self.connect_to_server()

    def send_file(self, server_addr, file_name):
        c = transfer_client.transfer_client(server_addr)
        c.get_file(file_name)

    def recv_file(self, file_type, extension):
        t = transfer_server.transfer_server(file_type, extension)
        t.save_file(file_type, file_data, extension)

    def connect_to_server(self):
        self.s.connect(self.client_addr)

    def send_message(self, message):
        self.s.send(message.encode('UTF-8'))
        self.s.close()

    def register_client(self, client, login):
        r = request_packet.request_packet()

    def invite(self, seq_num):
        r = request_packet.request_packet(1, self.sender_name, self.domain, self.protocol, self.port, self.sender_network_name, self.receiver_network_name, self.receiver_name, seq_num, self.subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def ack(self, seq_num):
        r = request_packet.request_packet(4, self.sender_name, self.domain, self.protocol, self.port, self.sender_network_name, self.receiver_network_name, self.receiver_name, seq_num, self.subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet

    def send_data(self, data):
        p = payload.payload()

    def bye(self, seq_num):
        r = request_packet.request_packet(2, self.sender_name, self.domain, self.protocol, self.port, self.sender_network_name, self.receiver_network_name, self.receiver_name, seq_num, self.subject, self.content_type, self.content_sub_type)
        packet = r.get_packet()
        return packet
