import socket
from peer import peer

class client(peer):
    __peer_ = None
    __client_address = ()

    __client_name = ''
    __domain = ''
    __protocol = ''
    __client_network_name = ''
    __content_type = ''
    __content_sub_type = ''

    def __init__(self, client_name, domain, protocol, client_network_name, content_type, content_sub_type):
        self.__peer_ = peer.peer(6050) # port for packet transmission
        self.__peer_.connect_to_server()

    def _exec_func(self, func, client_socket):
        if func[0] == '_register_server':
            return func[1](client_socket)
        else:
            return func[1](client_socket, 'bat', 'bat') # Number of arguments

    # Send message by client

    def __set_client_name(self, client_name):
        self.__server_name = client_name

    def __get_client_name(self):
        return self.__client_name

    def __set_domain(self, domain):
        self.__set_domain = domain

    def __get_domain(self):
        return self.__domain

    def __set_client_network_name(self, client_network_name):
        self.__client_network_name = client_network_name

    def __get_client_network_name(self):
        return self.__client_network_name

    def __set_content_type(self, content_type):
        self.__content_type = content_type

    def __get_content_type(self):
        return self.__content_type

    def __set_content_sub_type(self, content_sub_type):
        self.__content_sub_type = content_sub_type

    def __get_content_sub_type(self):
        return self.__content_sub_type

    def __set_protocol(self, protocol):
        self.__protocol = protocol

    def __get_protocol(self):
        return self.__protocol