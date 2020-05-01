import re
import os
from urllib.parse import urlparse

def encode_url(url):
    if re.match(r"https?://.+", url) is None:
        url = "http://" + url
    parsed = urlparse(url)
    if parsed.netloc == 'vpn.just.edu.cn':
        return url
    path = parsed.path
    if path == '':
        path = '/'
    ssl_flag = ''
    if parsed.scheme == 'https':
        ssl_flag = ',SSL'
    paths = os.path.split(path)
    filename = paths[1]
    if re.match(r'.+\.php', filename, re.IGNORECASE) is not None:
        path = paths[0]
    else:
        filename = ''
    if path[-1] != '/':
        path += '/'
    encoded_url = "https://vpn.just.edu.cn%s,DanaInfo=%s%s+%s?%s"%(path, parsed.netloc, ssl_flag, filename, parsed.query)
    return encoded_url

            
