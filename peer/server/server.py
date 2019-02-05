from peer import peer
import socket

class server(peer):
    __peer_ = None
    __server_address = ()
    __max_num_of_clients = 1
    __buff_size = 8192

    def __init__(self, port=6050, max_num_of_clients=1, buff_size=8192):
        self.__peer_ = peer.peer()
        self.__set_port(port)
        self.__set_max_num_of_clients(max_num_of_clients)
        self.__set_buff_size(buff_size)
        self.__set_server_address()

    def _create_server(self, func):
        print('Started transfer_tests server at address:' + str(self.__get_server_address()))
        self.__s.bind(self.__get_server_address())
        self.__s.listen(self.__get_max_num_of_clients())
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
