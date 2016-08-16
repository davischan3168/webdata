#! usr/bin/python
#coding=utf-8
"""
Get poem from http://www.gushiwen.org/
classify by chaodai, and the insert mysql 
database SDD and table gushiwen.

"""
__author__ = 'Davis'
import sys,os,time
import lxml.html
from lxml import etree
import requests,json,MySQLdb
import re
try:
    from io import StringIO
except:
    from pandas.compat import StringIO
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

def write_file(path,cont):
    with open(path,'a') as f:
        f.write(cont)
        f.flush
    return
def writePoemBySql(title,author,content):
    conn = MySQLdb.connect(host="localhost", port=3306, user='root', passwd='801019', db='SDD', charset="utf8")
    cur = conn.cursor()
    cur.execute("insert into gushiwen(title,author,content) value(%s, %s, %s)",[title.encode('utf-8'), author.encode('utf-8'),content.encode('utf-8')])
    conn.commit()
    cur.close()
    conn.close()
        
def _get_gushi(url):
    r=requests.get(url)
    r=r.text
    cpn=re.findall(r'p=\d+',url)[0].split('=')[1]
    print('Getting page %s data'%cpn)
    html=lxml.html.parse(StringIO(r))
    res=html.xpath("//div[@class=\"sons\"]")
    for p in res:
        title=p.xpath("p[1]/a/text()")[0]
        author=p.xpath("p[2]/text()")[0]
        content=p.xpath("p[3]/text()")[0]
        writePoemBySql(title,author,content)
    nextpage=html.xpath("//div[@class=\"pages\"]/a[last()]/@href")
    npn=re.findall(r'p=\d+',nextpage[0])[0].split('=')[1]
    if float(npn)>float(cpn):
        nexturl='http://so.gushiwen.org'+nextpage[0]
        try:
            _get_gushi(nexturl)
        except:
            print("failed to get page %s poem"%pageno)
    return

def get_mainv1(url):
    _get_gushi(url)
    return

def get_main_all(url):
    r=requests.get(url)
    r=r.text
    html=lxml.html.parse(StringIO(r))
    urls=html.xpath("//div[@class=\"main2\"]/div/a/@href")
    names=html.xpath("//div[@class=\"main2\"]/div/a/text()")
    listt=list(zip(urls,names))
    for ll in listt:
        print('Getting %s\' poem'%ll[1])
        try:
            _get_gushi(ll[0])
        except:
            pass
    return

url='http://www.gushiwen.org/'
urlv1='http://so.gushiwen.org/type.aspx?p=1&c=%E5%94%90%E4%BB%A3'#tangshi,finished
urlv2='http://so.gushiwen.org/type.aspx?p=1&c=%E5%AE%8B%E4%BB%A3'#songci,xianqin
urlv3='http://so.gushiwen.org/type.aspx?p=1&c=%E9%87%91%E6%9C%9D'#jinchao
#were finished,
#get_mainv1(urlv3)
get_main_all(url)
