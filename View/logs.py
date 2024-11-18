import logging
from logging.handlers import TimedRotatingFileHandler
import os
from datetime import datetime

def setup_logging(log_level=logging.INFO, rotation_period='d', interval=1):
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_filename = os.path.join(log_dir, f'logs_{datetime.now().strftime("%d-%m-%y-%H-%M-%S")}.log')

    logger = logging.getLogger()
    logger.setLevel(log_level)

    handler = TimedRotatingFileHandler(log_filename, when=rotation_period, interval=interval)
    handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
