import socket

class peer:
    __db = None
    __s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __port = 6050
    __client_address = ()
    __server_address = ()

    def __init__(self, port=6050):
        self.__set_port(port)
        self.__set_client_address()

    def connect_to_server(self):
        self.__s.connect(self.__client_address)

    def _send_message(self, message):
        message = message.encode('UTF-8')
        self.__s.send(message)

    def _receive_message(self, client_socket):
        message = client_socket.recv(self.__get_buff_size()).decode('UTF-8')
        return message

    def __set_port(self, port):
        self.__port = port

    def __get_port(self):
        return self.__port

    def __set_client_address(self):
        self.__client_address = (socket.gethostbyname(socket.gethostname()), self.__get_port())

    def __get_client_addr(self):
        return self.__client_address

    def __set_server_address(self):
        self.__server_address = (socket.gethostbyname(socket.gethostname()), self.__get_port())

    def __get_server_address(self):
        return self.__server_address

    def __set_max_num_of_clients(self, max_num_of_clients):
        self.__max_num_of_clients = max_num_of_clients

    def __get_max_num_of_clients(self):
        return self.__max_num_of_clients

    def __set_buff_size(self, buff_size):
        self.__buff_size = buff_size

    def __get_buff_size(self):
        return self.__buff_size