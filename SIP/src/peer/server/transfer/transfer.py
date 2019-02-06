import datetime
from random import choice
from string import digits
from peer.server.server import server

class transfer(server):
    __s = None

    __file_type = None
    __extension = None

    def __init__(self, file_type, extension):
        self.__set_file_type(file_type)
        self.__set_extension(extension)
        self.__s = server(6051, 10)
        self.__s._create_server((self._transfer_data.__name__, self._transfer_data))

    def _transfer_data(self, client_socket):
        file_size = client_socket.recv(self.__buff_size)
        file_parts = int(file_size / self.__buff_size)
        remaining_file_size = file_size % self.__buff_size
        file_data = b''
        print('Transfer in progress')
        for i in range(0, file_parts):
            file_data += client_socket.recv(self.__buff_size)
        file_data += client_socket.recv(remaining_file_size)
        print('Transfer complete')
        self._save_file(file_data)

    def _save_file(self, file_data):
        file_name = self.__get_file_type() + ''.join(choice(digits) for _ in range(8)) + ''.join(datetime.date.today().isoformat().split('-')) + '.' + self.__get_extension()
        try:
            f = open(file_name, 'rb')
            f.write(file_data)
            print('File write complete')
        except Exception:
            print('Unable to write file')
        finally:
            f.close()

    def __set_file_type(self, file_type):
        self.__file_type = file_type

    def __get_file_type(self):
        return self.__file_type

    def __set_extension(self, extension):
        self.__extension = extension

    def __get_extension(self):
        return self.__extension