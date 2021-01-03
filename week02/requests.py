# 使用requests库获取N1语法内容
import requests
from pathlib import *
import sys
# PEP-8
# Google Python 风格指引

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
header = {'user-agent':ua}

myurl = 'https://jn1et.com/tag/n1/'

try:
    response = requests.get(myurl, headers=header)
    selector = etree.HTML(response.text)

    #print(response.text)
    title = selector.xpath('//div[@class="entry-card-content card-content e-card-content"]/h2[@class="entry-card-title card-title e-card-title] [@itemprop="headline""]/text()')

    print(title)

except requests.exceptions.ConnectTimeout as e :
    print(f"requests库超时")
    sys.exit(1)

# 将网页内容改为存入文件
# print(response.text)

# 获得python脚本的绝对路径
p = Path(__file__)
pyfile_path = p.resolve().parent
# 建立新的目录html
html_path= pyfile_path.joinpath('html')

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('jn1et.html')

# 上下文管理器
try:
    with open(page, 'w',  encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f'文件无法打开,{e}')
except IOError as e:
    print(f'读写文件出错,{e}')
except Exception as e:
    print(e)