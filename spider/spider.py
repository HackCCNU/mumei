# coding: utf-8
import os
import redis
import requests

# rds-存储爬虫爬取学号、姓名信息
# info: {name: [sid]}
rds = redis.StrictRedis(host="localhost", port=6389, db=0)
# url-爬取的源地址, thanks@2bab
url = os.getenv("MUMEIURL")

rds.hset('info', '_placeholder', [])


def spider(start, end):
    """
    spider: 爬虫 
    -- start: 起始学号
    -- end: 终止学号+1
    """
    for sid in range(int(start), int(end)):
        # cout << "fuck %s" % sid 
        print "fuck %s\n" % sid
        r = requests.get(url.format(sid=str(sid)))
        if r.json() is None:
            continue
        name = r.json()[-1].get('userName')
        sids = [sid]
        if name in rds.hkeys('info'):
            sids = eval(rds.hget('info', name))
            sids.append(sid)
        rds.hset('info', name, str(sids))
        rds.save()
        print "%s done!\n" % sid

def start():
    """
    启动爬虫
    """
    start = "2014010001"
    end = "2014214841"
    spider(start, end)

if __name__ == '__main__':
    start()
