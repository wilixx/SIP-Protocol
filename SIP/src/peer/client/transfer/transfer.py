import client

class transfer(client):

    __client_ = None

    def __init__(self, client_name, domain, client_network_name, content_type, content_sub_type, protocol='TCP'):
        self.__client_ = client.client(client_name, domain, client_network_name, content_type, content_sub_type, protocol) # Add client details
        # Save media details using client

    # Send message by client

    def _send_file(self, file_data):
        self.__c._send_message(file_data)

    def _get_file(self, file_name):
        f = open(file_name, 'rb')
        try:
            file_data = f.read()
            size = str(len(file_data))
            self.__c._send_message(size)
            self._c._send_file(file_data)
            print('Transferred file ' + file_name)
        except Exception as e:
            print("Unable to read file")
        finally:
            self.f.close()