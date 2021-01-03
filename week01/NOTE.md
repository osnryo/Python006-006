1、已完成Python3.7和3.9环境安装，已配置pip。优先运行的为3.7版本
2、VS Code和Pycharm两个都有安装，并可以成功运行代码


# week1 homework

# 练习日志库
import logging

logging.basicConfig(filename='userlog',
                    level=logging.debug,
                    datefmt="%Y-%m-%d %H:%M:%S",
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s'
                    )

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# 练习随机数库
import random

random.randrange(0,101,2)

random.choice(['red', 'blue', 'orange'])

random.sample(['1', '2', '3', '4', '5'], k=4)

# 练习json库
import json

json.loads('[foo, {"bar":["barx", null, 1.0, 3]}]')
json.dump("[foo, {"bar":["barx", null, 1.0, 3]}]")

# 练习路径库
import pathlib

import os
os.path.abspath('test.log')

path = '/user/local/a.txt'

os.path.basename(path)

os.path.dirname(path)

os.path.exists('/etc/passwd')

os.path.isfile('/etc/passwd'))

os.path.isdir('/etc/passwd'))

os.path.join('a','b')



