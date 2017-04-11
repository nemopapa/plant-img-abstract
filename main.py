# -*-encoding:utf-8-*-
# python 2.7
__author__='NemoPapa'
import re
import time
import os
import requests
import threading
from bs4 import BeautifulSoup
import random
from config import (
    PLANT_SITES, PLANT_DEST, PLANTURL_DEST,
    FETCH_TIMEOUT,POOL_SIZE,REFERER_LIST,
    USER_AGENT_LIST
)
from thread_pool.pool import Pool


# 某多肉网站爬虫类，爬图片及简介.存取为文本格式。
class succulent_plant:
    # 初始化
    def __init__(self):
        self.totalurl=[]
        self.planturl=PLANTURL_DEST
        self.seedurl =PLANT_SITES
        self.save_path = PLANT_DEST
        self.timeout = FETCH_TIMEOUT
        self.lock = threading.Lock()
        self.headers = {'User-Agent': random.choice(USER_AGENT_LIST),
                        'Referer': random.choice(REFERER_LIST)}
    #爬数据
    def start(self,index):
        url_current = "http://www.mengsang.com/duorou/list_1_%s.html" %(index)
         # 异常处理，页面响应超时
        try:
            quest = requests.get(url_current, timeout=self.timeout,headers=self.headers)
            response = quest.content.decode('gbk','ignore')
            soup = BeautifulSoup(response, 'lxml')
            if quest.status_code == 200:
                #bs4匹配查找
                for urlimg in soup.find_all('a', class_='preview'):
                    imgurl=urlimg['data-preview']
                    Abstracturl = urlimg['href']
                    PicName = urlimg['title']
                    replaceBR = re.compile('/')  # 替换名称中含有/的字符
                    PicName = re.sub(replaceBR, "2", PicName)
                    if Abstracturl in self.totalurl:
                        continue
                    else:
                        with self.lock:
                            with open(self.planturl,'a') as fs:
                                fs.write(Abstracturl+'\r\n')
                                print Abstracturl
                            self.SaveImg(imgurl, PicName)
                            self.SaveAbstract(Abstracturl, PicName)
        except Exception , e:
            print e
    #存图片
    def SaveImg(self, pic_url, PicName):  # 参数：url图片链接，PicName：图片名
        try:  # 异常处理，保证程序出现异常继续执行
            res = requests.get(pic_url, timeout=self.timeout,headers=self.headers)
            save_img_path = os.path.join(self.save_path, PicName + ".jpg")
            # 保存下载的图片
            if res.status_code == 200:
                with open(save_img_path, 'wb') as fs:
                    for chunk in res.iter_content(1024):
                        fs.write(chunk)
                    print 'Had Saved %s Pic!' % PicName
        except Exception, e:
            print e
            return
        finally:
            return
    #存简介
    def SaveAbstract(self, abstract_url, PicName):  # 参数：url简介链接，PicName：图片名
        try:  # 异常处理，保证程序出现异常继续执行
            res = requests.get(abstract_url, timeout=self.timeout,
                               headers=self.headers).content.decode('gbk','ignore')
            save_abstract_path = os.path.join(self.save_path, PicName + ".txt")
            soup = BeautifulSoup(res, 'lxml')
            with open(save_abstract_path, "wb") as fop:
                for i in soup.find_all("div", attrs={"class": "imgCenter"}, limit=1):
                    result = i.stripped_strings
                    for item in result:
                            fop.write(item.encode('utf-8') + '\r\n')
            print 'Had Saved %s Abstract!' % PicName
        except Exception , e:
            print e
            return
        finally:
            return

    #从首页判断需爬页码
    def lastpage(self,seedurl):
        print u"判断需要爬多少页码数据..."
        res = requests.get(seedurl, timeout=self.timeout,headers=self.headers)
        response=res.content.decode('gbk','ignore')
        soup = BeautifulSoup(response, 'lxml')
        for pages in soup.find_all("a"):
            page = pages.stripped_strings
            for result in page:
                if result == u'末页':
                    totalpage=re.findall(r"\d+", pages['href'])[1]
                    print "Total Pages is: %s" % (totalpage)
                    return totalpage



def main():
    """ main """
    spider = succulent_plant()
    starttime = time.clock()
    spider.totalurl = list(map(str.strip, open(spider.planturl).readlines()))
    totalpage=spider.lastpage(spider.seedurl)
    print u"开始爬取"+totalpage+u'页数据...'
    pool = Pool(size=POOL_SIZE)
    pool.add_tasks([(spider.start,(index,)) for index in range(1,int(totalpage)+1)])
    pool.run()
    endtime = time.clock()
    print "all time is: %f s" % (endtime - starttime)

if __name__ == "__main__":
    main()

