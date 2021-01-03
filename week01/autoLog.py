# week1 homework

import logging
from datetime import *
import os

current_time = datetime.now().strftime('%Y-%m-%d')
path = r'/var/log/python-{}'.format(current_time)
if not os.path.exists(path):
    os.mkdir(path)

logging.basicConfig(
    filename = path + 'test.log', 
    level = logging.DEBUG, 
    filemode = 'a',
    datefmt = '%Y-%m-%d %H:%M:%S',
    format = '%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')


def debug_msg(msg):
    logging.debug(msg)