import logging


class logger:

    logger = None

    def __init__(self, logger_name, file_name):
        self.set_logger_name(logger_name)
        self.get_log_file_name(file_name)

    def set_logger_name(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

    def get_log_file_name(self, file_name):
        # create a file handler
        handler = logging.FileHandler(file_name)
        handler.setLevel(logging.INFO)
        # add the handlers to the logger
        self.logger.addHandler(handler)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

    def log_print(self, message):
        self.logger.info(message)
        print(message)
