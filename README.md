# plant-img-abstract
一个爬取多肉知识的小爬虫，新手，写的很乱。

# 描述
用来采集某多肉网站图片和简介。源于想获取网站上的一些资料，最近一年老婆喜欢养多肉，买了很多
，有的都不知道叫什么？手动保存麻烦，只好依靠爬虫了。python确实强大，各种代码都有，学习起来快捷方便，哈哈。

## config.py
相关配置，例如采集网站列表、超时时间等。

## main.py
采集器主程序，采集网站内容，输出目录见配置文件。

## 依赖
依赖[thread_pool](https://github.com/kaito-kidd/thread_pool)。

## 使用
    git clone https://github.com/nemopapa/plant-img-abstract.git

    # 根据配置的网站采集
    python main.py

## 说明
可根据需要调整'Pool'的大小,详情见'config.py'。
