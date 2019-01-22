import socket

class transfer_client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6051
    server_addr = ()

    def __init__(self, server_addr):
        self.server_addr = (server_addr, self.port)
        self.connect_to_server()

    def connect_to_server(self):
        self.s.connect(self.server_addr)

    def send_message(self, message):
        self.s.send(message)
        self.s.close()

    def read_file(self, file_name):
        f = open(file_name, 'rb')
        try:
            data = f.read()
            self.send_message(data)
            print('Transferred file ' + file_name)
        except FileException:
            print("Unable to read file")
        f.close()
