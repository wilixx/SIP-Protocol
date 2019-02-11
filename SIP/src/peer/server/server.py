from peer import peer


class server:
    __peer_ = None
    __server_address = ()
    __max_num_of_clients = 1
    __buff_size = 8192

    __server_name = ''
    __domain = ''
    __protocol = ''
    __port = ''
    __server_network_name = ''
    __content_type = ''
    __content_sub_type = ''

    def __init__(self, server_name, domain, port, server_network_name,
                 content_type, content_sub_type, max_num_of_clients=1,
                 buff_size=8192):
        self.__peer_ = peer('TCP', 6050)
        self.__set_max_num_of_clients(max_num_of_clients)
        self.__set_buff_size(buff_size)
        self.__set_server_address()
        self.__set_server_name(server_name)
        self.__set_domain(domain)
        self.__set_port(port)
        self.__set_server_network_name(server_network_name)
        self.__set_content_type(content_type)
        self.__set_content_sub_type(content_sub_type)

    def create_server(self, func):
        print('Started server at address:' + str(self._get_server_address()))
        self.__peer_._socket_bind(self._get_server_address())
        self._socket_listen(self._get_max_num_of_clients())
        try:
            while True:
                (client_socket, addr) = self._socket_accept()
                self._exec_func(func, client_socket)
        except KeyboardInterrupt:
            print('Closed socket')
        finally:
            self._socket_close()

    def _exec_func(self, func, client_socket):
        if func[0] == '_register_server':
            return func[1](client_socket)
        else:
            return func[1](client_socket, 'bat', 'bat')

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

    def __set_max_num_of_clients(self, max_num_of_clients):
        self.max_num_of_clients = max_num_of_clients

    def _get_max_num_of_clients(self):
        return self.max_num_of_clients

    def __set_buff_size(self, buff_size):
        self.buff_size = buff_size

    def _get_buff_size(self):
        return self.buff_size

    def __set_server_address(self):
        self.__server_address = self.__peer_.get_s_address()

    def _get_server_address(self):
        return self.__server_address
