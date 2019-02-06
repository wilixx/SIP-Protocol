from src.peer import peer

class client(peer):
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

    def __init__(self, username, password, client_name, domain, protocol, client_network_name, content_type, content_sub_type):
        self.__peer_ = peer.peer(6050) # port for packet transmission, username, password
        self.__set_username(username)
        self.__set_password(password)
        self.__set_client_name(client_name)
        self.__set_domain(domain)
        self.__set_port()
        self.__set_protocol(protocol)
        self.__set_client_network_name(client_network_name)
        self.__set_content_type(content_type)
        self.__set_content_sub_type(content_sub_type)

    def _exec_func(self, func, client_socket):
        if func[0] == '_register_server':
            return func[1](client_socket)
        else:
            return func[1](client_socket, 'bat', 'bat') # Number of arguments

    def __set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.username

    def __set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def __set_client_address(self):
        self.__client_address = self.__peer_.get_s_address()

    def get_client_addr(self):
        return self.__client_address

    def __set_client_name(self, client_name):
        self.__server_name = client_name

    def get_client_name(self):
        return self.__client_name

    def __set_domain(self, domain):
        self.__set_domain = domain

    def get_domain(self):
        return self.__domain

    def __set_port(self):
        self.__port = str(self.__peer_.get_port())

    def __get_port(self):
        return str(self.__port)

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