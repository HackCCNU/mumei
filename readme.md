# 无名

> CCNU Central Picture Database

+ [project index ⚡️ ](http://p.muxixyz.com)

## ⚡️ How 2 use
### 1.请先登录
跳转登录华中师范大学信息服务平台

### 2.开始搜索
搜同学的名字, 获取<br/>

+ 美美的证件照
+ 学号
+ 专业信息
+ 爱吃什么...

你还可以知道和你重名的同学,, 长啥样.....<br/>
目前爬了 **2016**, **2015**, **2014**, **2013** 级😄 <br/>

## ⚡️ How 2 run
### python develop server
**1.设置环境变量** <br/>

+ MUMEIURL: console api url
+ MUMEIURLPRE: photo url
+ REDISHOST: redis server host

**2.启动** <br/>
启动server

    $ python manage.py runserver

启动爬虫

    $ python spider/spider.py

### gunicorn server in docker
**1.设置环境变量文件** <br/>
mumei.env

    MUMEIURL=console api url
    MUMEIURLPRE=photo url
    REDISHOST=redis server host

**2.启动**<br/>
启动server

    $ docker-compose up -d app

启动爬虫

    $ docker-compose up -d spider

## ⚡️ About this project
Just curious and fun. <br/>
学长... 我很好奇:) 这个项目就是一次hack, 只是为了好玩, 如果涉及隐私,
对此表示抱歉:(<br/>
this is life, this is love<br/>

## ⚡️ License(WTFPL)


    (The WTFPL)

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004
    
    Copyright (C) 2016 neo1218 (https://github.com/neo1218)
    
    Everyone is permitted to copy and distribute verbatim or modified
    copies of this license document, and changing it is allowed as long
    as the name is changed.
    
               DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
      TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
    
     0. You just DO WHAT THE FUCK YOU WANT TO.

