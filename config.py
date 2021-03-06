# coding: utf8

"""配置
"""

# 采集的站点
PLANT_SITES ='http://www.mengsang.com/duorou/list_1_1.html'

# referer list
REFERER_LIST = [
    "http://www.google.com/",
    "http://www.bing.com/",
    "http://www.baidu.com/",
]

# User-Agent list
USER_AGENT_LIST = [
    'Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
    'Microsoft Internet Explorer/4.0b1 (Windows 95)',
    'Opera/8.00 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
    'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
]


# 采集超时时间
FETCH_TIMEOUT = 10

# 采集输出位置
PLANT_DEST = r"D:\python\test"

#Plant url存储位置
PLANTURL_DEST = r"D:\python\test\planturl.txt"

# 测试代理线程池大小
POOL_SIZE = 50
