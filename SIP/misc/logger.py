import logging

logger = logging.getLogger('Packets Log')
logger.setLevel(logging.INFO)


def get_log_file_name(file_name):
    # create a file handler
    handler = logging.FileHandler(file_name)
    handler.setLevel(logging.INFO)
    # add the handlers to the logger
    logger.addHandler(handler)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)


def log_print(message):
    logger.info(message)
    print(message)
