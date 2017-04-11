## 描述
    一个爬取多肉知识的小爬虫，新手，写的很乱。
    最近一年老婆喜欢养多肉，买了很多，有的都不知道叫什么？手动保存网站上的一些资料，麻烦！
    只好依靠万能的爬虫了。python确实强大，各种示范代码都有，学习起来快捷方便，哈哈。

## config.py
    相关配置，例如采集网站列表、超时时间等。
    可根据需要调整'Pool'的大小,详情见'config.py'。

## main.py
    采集器主程序，采集网站内容，输出目录见配置文件。

## 依赖
    依赖[thread_pool](https://github.com/kaito-kidd/thread_pool)。
    pip install bs4
    pip install lxml
    pip install requests
    
## 使用
    git clone https://github.com/nemopapa/plant-img-abstract.git

    # 根据配置的网站采集
    python main.py
