# -*-encoding:utf-8-*-
# python 2.7
import re
import time
from threading import Thread
import requests
import os
from bs4 import BeautifulSoup
import csv
import random



# 某多肉网站爬虫类，爬图片及简介.存取为文本格式。
class succulent_plant:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.PlantName=[]
        self.filename=r"D:\python\code\test\good_proxy_list.txt"
        self.plantfilename=r"D:\python\code\test\plant_list.txt"
        # 多肉网站下载种子
        self.seedurl = 'http://www.mengsang.com/duorou/list_1_1.html'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 爬取内容存储路径
        self.save_path = os.path.join(os.path.abspath('.'), "test")
        if os.path.isdir(self.save_path) is False:#Test文件夹不存在就新建
            os.mkdir(self.save_path)
        #随机user_agent
        self.user_agent = [ \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", \
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        # 初始化headers
        self.headers = {'User-Agent': random.choice(self.user_agent)}

    def SaveImg(self, pic_url, PicName):  # 参数：url图片链接，PicName：图片名
        try:  # 异常处理，保证程序出现异常继续执行
            res = requests.get(pic_url, timeout=30, headers=self.headers)
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

    def SaveAbstract(self, abstract_url, PicName):  # 参数：url简介链接，PicName：图片名
        try:  # 异常处理，保证程序出现异常继续执行
            res = requests.get(abstract_url, timeout=30, headers=self.headers,
                               proxies=self.proxies).content.decode('gbk','ignore')
            time.sleep(1)
            save_abstract_path = os.path.join(self.save_path, PicName + ".txt")
            soup = BeautifulSoup(res, 'lxml')
            self.PlantName.append(PicName)
            fw = open(save_abstract_path, "wb")
            for i in soup.find_all("div", attrs={"class": "imgCenter"}, limit=1):
                result = i.stripped_strings
                #row=[]
                #row.append(PicName.encode('gbk'))
                for item in result:
                    fw.write(item.encode('utf-8') + '\r\n')
                    #row.append(item.encode('gbk'))
                #self.writer.writerow(row)
            fw.close()
            print 'Had Saved %s Abstract!' % PicName
        except Exception , e:
            print e
            return
        finally:
            return

    def load_proxies(self, filename):
        """从文件加载有效代理 """
        proxy_list = []
        with open(filename) as fip:
            for line in fip:
                proxy_list.append(line.split('|')[0])
        proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
        self.proxies = {'http': proxy_ip}
        return self.proxies

    def main(self):
        url_list = []
        url_unlist = []
        url_count = 0
        url_list.append(self.seedurl)
        start = time.clock()
        #csvfile = file(os.path.join(self.save_path,'Abstract.csv'), 'wb')
        #self.writer = csv.writer(csvfile)
        while url_list.__len__() > 0:
            # 获取地址列表第一条
            url_current = url_list.pop(0)
            url_unlist.append(url_current)
            # 异常处理，页面响应超时
            try:
                spider.load_proxies(self.filename)
                print spider.load_proxies(self.filename)
                quest = requests.get(url_current, timeout=10,
                                           headers=self.headers,proxies=self.proxies)
                response = quest.content.decode('gbk','ignore')
                soup = BeautifulSoup(response, 'lxml')
                if quest.status_code == 200:
                    # 将列表中不存在的页码链接添加到url_list中
                    for links in soup.find_all("div", attrs={"class": "fRight cRight"}):
                        link = links.find_all("a", href=True)
                        for item in link:
                            url_next_page = "http://www.mengsang.com/duorou/" + item['href']
                            url_unlist.extend(url_list)
                            if url_next_page not in url_unlist:
                                url_list.append(url_next_page)
                                #print "Next Page:", url_next_pagetitle
                    # 新版采用多线程，对每个页面建立一个线程进行爬取图片
                    threads = []
                    i=0
                    for urlimg in soup.find_all('a',class_='preview'):
                        #imgurl=urlimg['data-preview']
                        Abstracturl=urlimg['href']
                        PicName=urlimg['title']
                        replaceBR = re.compile('/')  # 替换名称中含有/的字符
                        PicName = re.sub(replaceBR, "2", PicName)
                        i+=1
                        f = open(self.plantfilename, "r")
                        lines = f.readlines()  # 读取全部内容
                        if PicName not in lines:
                            #t1 = Thread(target=self.SaveImg, args=(imgurl,PicName))
                            #threads.append(t1)
                            t2 = Thread(target=self.SaveAbstract, args=(Abstracturl,PicName))
                            threads.append(t2)
                        for t in threads:
                            t.setDaemon(True)
                            t.start()
                        for t in threads:
                            t.join()
                        print "There Are", i, "Imgs On Page", url_current
                        url_count += 1
                        print "Had View", url_count, "Pages"
            except Exception , e:
                print e
                continue
        fs = open(self.plantfilename, "a")
        for plant in self.PlantName:
            fs.write(plant.encode('utf-8')+'\r\n')
        fs.close()
        end = time.clock()
        print "all time is: %f s" % (end - start)
    # 开始方法
    def start(self):
        print u"正在读取网站内容"
        if __name__ == '__main__':
            self.main()


spider = succulent_plant()
spider.start()
