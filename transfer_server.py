import socket

class transfer_server:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 6051

    server_addr = (socket.gethostname(), port)
    max_num_of_clients = 1
    buff_size = 4096

    def __init__(self):
        self.create_server()

    def create_server(self):
        print('Started transfer server at port: ' + str(self.port))
        self.s.bind(self.server_addr)
        self.s.listen(self.max_num_of_clients)
        try:
            while True:
                (client_socket, addr) = self.s.accept()
                msg = self.s.recv(self.buff_size)
                print(msg)
                client_socket.close()
        except KeyboardInterrupt or Exception:
                print('Closed socket')
        finally:
                self.s.close()
