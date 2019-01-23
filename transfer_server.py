import socket
from random import choice
from string import digits
import datetime

class transfer_server:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 6051

    server_addr = (socket.gethostname(), port)
    max_num_of_clients = 1
    buff_size = 4096

    def __init__(self, file_type, extension):
        self.create_server(file_type, extension)

    def create_server(self, file_type, extension):
        print('Started transfer server at port: ' + str(self.port))
        self.s.bind(self.server_addr)
        self.s.listen(self.max_num_of_clients)
        try:
            while True:
                (client_socket, addr) = self.s.accept()
                file_data = client_socket.recv(self.buff_size)
                self.save_file(file_type, file_data, extension)
        except KeyboardInterrupt or Exception:
                print('Closed socket')
        finally:
                self.s.close()

    def save_file(self, file_type, file_data, extension):
        file_name = file_type + ''.join(choice(digits) for _ in range(8)) + ''.join(datetime.date.today().isoformat().split('-')) + '.' + extension
        try:
            f = open(file_name, 'wb')
            f.write(file_data)
            print('Writing file completed')
        except FileException:
            print('Unable to write file')
        finally:
            f.close()
