from peer.peer import peer


class server:
    __peer_ = None
    __max_num_of_clients = 1

    __server_name = ''
    __domain = ''
    __protocol = ''
    __port = ''
    __server_network_name = ''
    __content_type = ''
    __content_sub_type = ''

    def __init__(self, server_name, domain, protocol, port,
                 server_network_name, content_type, content_sub_type,
                 max_num_of_clients=1):
        self.__peer_ = peer(protocol, int(port))
        self.__set_max_num_of_clients(max_num_of_clients)
        self.__set_server_name(server_name)
        self.__set_domain(domain)
        self.__set_protocol(protocol)
        self.__set_port(port)
        self.__set_server_network_name(server_network_name)
        self.__set_content_type(content_type)
        self.__set_content_sub_type(content_sub_type)

    def create_server(self, func):
        print('Started server at address:' + str(self.__peer_._get_s_address()))
        self.__peer_.socket_bind()
        if self.get_protocol() == 'TCP':
            self.__peer_.socket_listen(self._get_max_num_of_clients())
        try:
            while True:
                if self.get_protocol() == 'TCP':
                    (client_socket, addr) = self.__peer_.socket_accept()  # Create new thread for each client
                    self._exec_func(func, client_socket)
                if self.get_protocol() == 'UDP':
                    self._exec_func(func)
        except KeyboardInterrupt:
            print('Closed socket')
        finally:
            self.__peer_.socket_close()

    def _exec_func(self, func, client_socket=None):
        if func.__name__ == 'register_server':
            if client_socket is None:
                return func()
            else:
                return func(client_socket)

    def send_message(self, message, address=None, client_socket=None):
        protocol = self.get_protocol()
        self.__peer_.server_send_message(protocol, message, client_socket,
                                         address)

    def receive_message(self, client_socket=None):
        protocol = self.get_protocol()
        message = self.__peer_.server_receive_message(client_socket)
        return message

    def __set_server_name(self, server_name):
        self.__server_name = server_name

    def get_server_name(self):
        return self.__server_name

    def __set_domain(self, domain):
        self.__set_domain = domain

    def get_domain(self):
        return self.__domain

    def __set_server_network_name(self, server_network_name):
        self.__server_network_name = server_network_name

    def get_server_network_name(self):
        return self.__server_network_name

    def __set_content_type(self, content_type):
        self.__content_type = content_type

    def get_content_type(self):
        return self.__content_type

    def __set_content_sub_type(self, content_sub_type):
        self.content_sub_type = content_sub_type

    def get_content_sub_type(self):
        return self.__content_sub_type

    def __set_port(self, port):
        self.__port = port

    def get_port(self):
        return self.__port

    def __set_protocol(self, protocol):
        self.__protocol = protocol

    def get_protocol(self):
        return self.__protocol

    def __set_max_num_of_clients(self, max_num_of_clients):
        self.max_num_of_clients = max_num_of_clients

    def _get_max_num_of_clients(self):
        return self.max_num_of_clients
