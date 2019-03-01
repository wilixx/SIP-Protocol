import socket


class peer:

    __db = None
    __s = socket

    __protocol = ''
    __port = 5060
    __s_address = ()
    __buff_size = 4096

    def __init__(self, protocol='TCP', port=5060, buff_size=4096):
        self.__set_protocol(protocol)
        self.__set_port(port)
        self.__set_buff_size(buff_size)
        self.__initialize_socket()
        self.__set_s_address()

    def __initialize_socket(self):
        if self._get_protocol() == 'TCP':
            self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            if self._get_protocol() == 'UDP':
                self.__s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            else:
                print('Unable to initialize socket')
                exit(0)

    def socket_bind(self):
        self.__s.bind(self._get_s_address())

    def socket_listen(self, backlog):
        self.__s.listen(backlog)

    def socket_accept(self):
        (client_socket, addr) = self.__s.accept()
        return (client_socket, addr)

    def socket_connect(self, server_address):
        self.__s.connect(server_address)

    def socket_close(self):
        self.__s.close()

    def client_send_message(self, message, address=None):
        message = message.encode('UTF-8')
        if address is None:
            self.__s.send(message) # Have to fix for TCP, it requires client_socket
        else:
            self.__s.sendto(message, address)

    def client_receive_message(self, protocol):
        if protocol == 'TCP':
            message = self.__s.recv(self._get_buff_size())  # Client socket.recv maybe be the correct method
        if protocol == 'UDP':
            message, addr = self.__s.recvfrom(self._get_buff_size())
        return message.decode('UTF-8')

    def server_send_message(self, protocol, message, client_socket=None,
                            address=None):
        message = message.encode('UTF-8')
        if protocol == 'TCP':
            client_socket.send(message)
        if protocol == 'UDP':
            self.__s.sendto(message, address)

    def server_receive_message(self, client_socket=None):
        if client_socket is None:
            message, addr = self.__s.recvfrom(self._get_buff_size())
        else:
            message = client_socket.recv(self._get_buff_size())
        return (message.decode('UTF-8'), addr)

    def __set_protocol(self, protocol):
        self.__protocol = protocol

    def _get_protocol(self):
        return self.__protocol

    def __set_port(self, port):
        self.__port = port

    def _get_port(self):
        return self.__port

    def __set_buff_size(self, buff_size):
        self.__buff_size = buff_size

    def _get_buff_size(self):
        return self.__buff_size

    def __set_s_address(self):
        self.__s_address = (socket.gethostbyname(socket.gethostname()),
                            self._get_port())

    def _get_s_address(self):
        return self.__s_address
