from SIP.src.peer.peer import peer
from SIP.src.packet.request.request import request


class client:
    __peer_ = None
    __client_socket_ = None
    __client_address = ()

    __username = ''
    __password = ''

    __client_name = ''
    __domain = ''
    __port = ''
    __protocol = ''
    __client_network_name = ''
    __content_type = ''
    __content_sub_type = ''

    def __init__(self, username, password, client_name, domain, protocol,
                 port, client_network_name, content_type, content_sub_type):
        self.__peer_ = peer(protocol, int(port))  # Protcol and port
        self.__set_username(username)
        self.__set_password(password)
        self.__set_client_name(client_name)
        self.__set_domain(domain)
        self.__set_port(port)
        self.__set_protocol(protocol)
        self.__set_client_network_name(client_network_name)
        self.__set_content_type(content_type)
        self.__set_content_sub_type(content_sub_type)

    def connect_to_server(self, server_address):
        self.__peer_.socket_connect(server_address)

    def disconnect_from_server(self):
        self.__peer_.socket_close()

    def send_message(self, message, address=None):
        self.__peer_.client_send_message(message, address) # Have to fix for TCP

    def receive_message(self, protocol):
        message = self.__peer_.client_receive_message(protocol)
        return message

    def __set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def __set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def __set_client_address(self):
        self.__client_address = self.__peer_._get_s_address()  # Check get_s_address

    def get_client_addr(self):
        return self.__client_address

    def __set_client_name(self, client_name):
        self.__client_name = client_name

    def get_client_name(self):
        return self.__client_name

    def __set_domain(self, domain):
        self.__domain = domain

    def get_domain(self):
        return self.__domain

    def __set_port(self, port):
        self.__port = port

    def get_port(self):
        return self.__port

    def __set_client_network_name(self, client_network_name):
        self.__client_network_name = client_network_name

    def get_client_network_name(self):
        return self.__client_network_name

    def __set_content_type(self, content_type):
        self.__content_type = content_type

    def get_content_type(self):
        return self.__content_type

    def __set_content_sub_type(self, content_sub_type):
        self.__content_sub_type = content_sub_type

    def get_content_sub_type(self):
        return self.__content_sub_type

    def __set_protocol(self, protocol):
        self.__protocol = protocol

    def get_protocol(self):
        return self.__protocol
