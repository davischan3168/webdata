#! usr/bin/python
#coding=utf-8 
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


def _get_Phetfiles(url):
    r=requests.get(url)
    r=r.text
    html=lxml.html.parse(StringIO(r))
    res=html.xpath("//table/tr/td[@class=\"simulation-list-item\"]")
    #data=[]
    for a in res:
        title=a.xpath("a/strong/span/text()")[0]#.os.path.split('/')[1]
        title=os.path.split(title)[1]
        url=a.xpath("a/@href")[0]
        url='https://phet.colorado.edu'+url
        _download_file(url,title)
        #print('the %s for the url %s'%(title,url))
        #data.append([title,url])
    return

def _download_file(url,name):
    r=requests.get(url)
    r=r.text
    html=lxml.html.parse(StringIO(r))
    url=html.xpath("//div[@class=\"simulation-main-image-panel\"]/a[2]/@href")[0]
    ftype=os.path.splitext(url)[1]
    url='https://phet.colorado.edu'+url
    path='/home/chen/文档/Phet/'+name+ftype
    path1=os.path.split(path)[0]
    if not os.path.exists(path1):
        os.mkdir(path1)
    if not os.path.exists(path):
        r = requests.get(url, stream=True)  
        with open(path, 'wb') as f:  
            for chunk in r.iter_content(chunk_size=1024):  
                if chunk: # filter out keep-alive new chunks  
                    f.write(chunk)  
                    f.flush()  
        print ('Download %s finished'%name)
    return

def get_Phetfiles(url):
    r=requests.get(url)
    text=r.text
    html=lxml.html.parse(StringIO(text))
    urls=html.xpath("//div[@class=\"link-holder\"]/ul/li[@class=\"nav-li\"]/div/a/@href")
    base='https://phet.colorado.edu'
    for url in urls:
        url=base+url
        _get_Phetfiles(url)
    return



    
url='https://phet.colorado.edu/zh_CN/simulations/category/new'
#https://phet.colorado.edu/zh_CN/simulations/category/new
get_Phetfiles(url)
