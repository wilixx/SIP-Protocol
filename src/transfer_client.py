import socket

class transfer_client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6051  # Encrypt communication
    server_addr = (socket.gethostbyname(socket.gethostname()), port)

    def __init__(self):
        self.connect_to_server()

    def connect_to_server(self):
        self.s.connect(self.server_addr)

    def send_file(self, file_data):
        self.s.send(file_data) #Just use tls over tcp here, can put an option by an arguement
        self.s.close()

    def get_file(self, file_name):
        f = open(file_name, 'rb')
        try:
            file_data = f.read()
            size = str(len(file_data))
            self.s.send(size.encode('UTF-8'))
            self.send_file(file_data)
            print('Transferred file ' + file_name)
        except Exception as e:
            print("Unable to read file")
        finally:
            f.close()
