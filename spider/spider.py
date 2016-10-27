# coding: utf-8
import os
import redis
import requests

# rds-存储爬虫爬取学号、姓名信息
# info: {name: [sid]}
rds = redis.StrictRedis(host=os.getenv("REDISHOST"), port=6389, db=0)
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
        r = requests.get(url.format(sid=str(sid)))
        if r.json() is None:
            continue
        name = r.json()[-1].get('userName')
        sids = [sid]
        if name.encode("utf-8") in rds.hkeys('info'):
            sids = eval(rds.hget('info', name))
            if sid not in sids:
                sids.append(sid)
        rds.hset('info', name, str(sids))
        rds.save()
        print "fuck %s\n" % str(sids)
    print "%s done!\n" % sid

def start():
    """
    启动爬虫
    """
    starts = ["2014211517", "2016214469", "2015210001", "2013210001"]
    ends = ["2014214841", "2016214643", "2015214781", "2013214858"]
    spider(2015211022, 2015211999)

if __name__ == '__main__':
    start()
