import socket

class server:

    __s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    __port = 6051
    __server_addr = ()
    _max_num_of_clients = 1
    __buff_size = 8192

    def __init__(self, port=6051, max_num_of_clients=1, buff_size=8192):
        self.__port = port
        self._set_max_num_of_clients(max_num_of_clients)
        self._set_buff_size(buff_size)
        self._set_server_addr()

    def _create_server(self, func):
        print('Started transfer server at address:' + self._get_server_addr())
        self.__s.bind(self.__server_addr)
        self.__s.listen(self._max_num_of_clients)
        try:
            while True:
                (client_socket, addr) = self.__s.accept()
                self._exec_func(func, client_socket)
        except KeyboardInterrupt:
            print('Closed socket')
        finally:
            self.__s.close()

    def _exec_func(self, func, client_socket):
        if func[0] == '_register_server':
            return func[1](client_socket)
        else:
            return func[1](client_socket, 'bat', 'bat')

    def _set_port(self, port):
        self.__port = port

    def _get_port(self):
        return str(self.__port)

    def _set_server_addr(self):
        self.__server_addr = (socket.gethostbyname(socket.gethostname()), self.__port)

    def _get_server_addr(self):
        return str(self.__server_addr)

    def _set_max_num_of_clients(self, max_num_of_clients):
        self._max_num_of_clients = max_num_of_clients

    def _get_max_num_of_clients(self):
        return str(self._max_num_of_clients)

    def _set_buff_size(self, buff_size):
        self.__buff_size = buff_size

    def _get_buff_size(self):
        return self.__buff_size