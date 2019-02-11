class payload:
    __payload = ''

    def __init__(self, version, sender_name, session_id, country_code,
                 ip_type, domain, ip_address, media_type, protocol_id,
                 media_transfer_type, protocol, port, modulation_type,
                 modulation_port, session_name='SESSION SDP'):
        self.__make_payload(version, sender_name, session_id, country_code,
                            ip_type, domain, ip_address, media_type,
                            protocol_id, media_transfer_type, protocol, port,
                            modulation_type, modulation_port,
                            session_name='SESSION SDP')

    def get_payload(self):
        return self.__payload

    def __add_version(self, version):
        self.__payload += 'v=' + version + '\r\n'

    def __add_owner_details(self, sender_name, session_id, country_code,
                            ip_type, domain):  # Generation of session id
        self.__payload += 'o=' + sender_name + ' ' + session_id + ' ' + \
                          country_code + ' ' + ip_type + ' ' + domain + '\r\n'

    def __add_session_details(self, session_name='SESSION SDP'):
        self.__payload += 's=' + session_name + '\r\n'

    def __add_contact_details(self, country_code, ip_type, ip_address):
        self.__payload += 'c=' + country_code + ' ' + ip_type + ' ' + \
                          ip_address + '\r\n'

    def __add_time_details(self, start_time, stop_time):
        self.__payload += 't=' + start_time + ' ' + stop_time + '\r\n'

    def __add_media_details(self, media_type, protocol, media_transfer_type):
        # Protocol ID
        self.__payload += 'm=' + media_type + ' ' + protocol + ' ' + \
                          media_transfer_type + '\r\n'

    def __add_session_attributes(self, protocol_id, port, modulation_type,
                                 modulation_port):
        self.__payload += 'a=' + protocol + ':' + port + ' ' + \
                         modulation_type + '/' + modulation_port

    def __make_payload(self, version, sender_name, session_id, country_code,
                       ip_type, domain, ip_address, media_type, protocol_id,
                       media_transfer_type, protocol, port, modulation_type,
                       modulation_port, session_name='SESSION SDP'):
        self.__add_version(version)
        self.__add_owner_details(sender_name, session_id, country_code,
                                 ip_type, domain)
        self.__add_session_details(session_name)
        self.__add_time_details('0', '0')
        self.__add_contact_details(country_code, ip_type, ip_address)
        self.__add_media_details(media_type, protocol_id, media_transfer_type)
        self.__add_session_attributes(protocol, port, communication_port,
                                      transfer_port)
