import socket

class peer:

    __db = None
    __s = socket

    __protocol = ''
    __port = 6050
    __s_address = ()

    def __init__(self, protocol='TCP', port=6050):
        self.__set_protocol(protocol)
        self.__set_port(port)
        self.__initialize_socket()
        self.__set_s_address()

    def __initialize_socket(self):
        if self.get_protocol() == 'TCP':
            self.__s = self.__s.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            if self.get_protocol() == 'UDP':
                self.__s = self.__s.socket(socket.AF_INET, socket.SOCK_DGRAM)
            else:
                print('Unable to initialize socket')
                exit(0)

    def _socket_bind(self, server_address):
        self.__s.bind(server_address)

    def _socket_listen(self, backlog):
        self.__s.listen(backlog)

    def _socket_accept(self):
        (client_socket, addr) = self.__s.accept()
        return (client_socket, addr)

    def _socket_connect(self, client_address):
        self.__s.connect(client_address)

    def _socket_close(self):
        self.__s.close()

    def server_send_message(self, message):
        message = message.encode('UTF-8')
        self.__s.send(message)

    def server_receive_message(self):
        message = self.__s.recv(self.get_buff_size()).decode('UTF-8')
        return message

    def client_send_message(self, client_socket, message):
        message = message.encode('UTF-8')
        client_socket.send(message)

    def client_receive_message(self, client_socket):
        message = client_socket.recv(self.get_buff_size()).decode('UTF-8')
        return message

    def __set_protocol(self, protocol):
        self.__protocol = protocol

    def get_protocol(self):
        return self.__protocol

    def __set_port(self, port):
        self.__port = port

    def get_port(self):
        return self.__port

    def __set_s_address(self):
        self.__s_address = (socket.gethostbyname(socket.gethostname()), self.get_port())

    def get_s_address(self):
        return self.__s_address

    def __set_max_num_of_clients(self, max_num_of_clients):
        self.__max_num_of_clients = max_num_of_clients

    def get_max_num_of_clients(self):
        return self.__max_num_of_clients

    def __set_buff_size(self, buff_size):
        self.__buff_size = buff_size

    def get_buff_size(self):
        return self.__buff_size