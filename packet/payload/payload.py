class payload:
    __payload = ''

    def __init__(self):
        self.__make_payload()

    def get_payload(self):
        return self.__payload

    def __add_version(self, version):
        self.__payload += 'v=' + version

    def __add_owner_details(self, sender_name, session_id, country_code, ip_type, domain):
        self.__payload += 'o=' + sender_name + ' ' + session_id + ' ' + country_code + ' ' + ip_type + ' ' + domain

    def __add_session_details(self, session_name='SESSION SDP'):
        self.__payload += 's=' + session_name

    def __add_contact_details(self, country_code, ip_type, ip_address):
        self.__packet += 'c=' + country_code + ' ' + ip_type + ' ' + ip_address

    def __add_time_details(self, start_time, stop_time):
        self.__packet += 't=' + start_time + ' ' + stop_time

    def __add_media_details(self, media_type, protocol_id, media_transfer_type):
        self.__packet += 'm=' + media_type + ' ' + protocol_id + ' ' + media_transfer_type

    def __add_session_attributes(self, protocol, port, communication_port, transfer_port):
        self.__packet += 'a=' + protocol + ':' + port + ' ' + communication_port + ':' + transfer_port

    def __make_payload(self, version, sender_name, session_id, country_code, ip_type, domain, ip_address, media_type, protocol_id, media_transfer_type, protocol, port, communication_port, transfer_port, session_name='SESSION SDP'):
        self.__add_version(version)
        self.__add_owner_details(sender_name, session_id, country_code, ip_type, domain)
        self.__add_contact_details(country_code, ip_type, ip_address)
        self.__add_time_details('0', '0')
        self.__add_media_details(media_type, protocol_id, media_transfer_type)
        self.__add_session_attributes(protocol, port, communication_port, transfer_port)