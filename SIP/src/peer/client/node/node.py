import client
import database

class node(client):

    __client_ = None
    __db = None

    def __init__(self, client_name, domain, client_network_name, content_type, content_sub_type, protocol='TCP',):
        self.__client_ = client.client(client_name, domain, client_network_name, content_type, content_sub_type, protocol)
        self.__initialize_db()

    # Send message by client

    def _establish_session(self):
        self.__client_

    def __initialize_db(self):
        self.__db = database()  #Might have to add database_tests name