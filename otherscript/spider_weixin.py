 # -*- coding: utf-8 -*-
 
'''
整体思路是通过抓取搜狗的微信文章搜索引擎来完成
http://weixin.sogou.com/
2016-08-26 by ruansz
'''
 
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
 
try:
    from urllib import quote
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
except:
    from urllib.request import quote
from pyquery import PyQuery as pq
from selenium import webdriver
 
import requests
import time
import re
import json
 
 
class weixin_spider:
 
    def __init__(self, kw):
        ' 构造函数 '
        self.kw = kw
        # 搜狐微信搜索链接
        self.sogou_search_url = 'http://weixin.sogou.com/weixin?type=1&query=%s&ie=utf8&_sug_=n&_sug_type_=' % quote(self.kw)
 
        # 爬虫伪装UA
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 FirePHP/0refox/47.0 FirePHP/0.7.4.1'}
 
        # curl操作超时时长
        self.timeout = 5
 
        # 爬虫模拟在一个session中完成
        self.s = requests.Session()
 
    def get_search_result_by_kw(self):
        ' 调用搜狗微信搜索 '
        return self.s.get(self.sogou_search_url, headers=self.headers, timeout=self.timeout).content.decode('utf8')
 
    def get_wx_url_by_sougou_search_html(self, sougou_search_html):
        ' 根据返回sougou_search_html，从中获取公众号主页链接 '
        doc = pq(sougou_search_html)
        return doc('div[class="wx-rb bg-blue wx-rb_v1 _item"]').attr('href')
 
    def get_selenium_js_html(self, wx_url):
        ' 执行wx_url中的js渲染内容，并返回渲染后的html内容 '
        browser = webdriver.PhantomJS() 
        browser.get(wx_url) 
        time.sleep(3) 
        # 执行js得到整个dom 
        html = browser.execute_script("return document.documentElement.outerHTML")
        return html
 
    def parse_wx_articles_by_html(self, selenium_html):
        ' 从selenium_html中解析出微信公众号文章 '
        doc = pq(selenium_html)
        return doc('div[class="weui_msg_card"]')
 
    def switch_arctiles_to_list(self, articles):
        ' 把articles转换成数据字典 '
        articles_list = []
        i = 1
 
        if articles:
            for article in articles.items():
                self.log(u'开始整合(%d/%d)' % (i, len(articles)))
                articles_list.append(self.parse_one_article(article))
                i += 1
                # break
 
        return articles_list
 
 
    def parse_one_article(self, article):
        ' 解析单篇文章 '
        article_dict = {}
 
        article = article('.weui_media_box[id]')
 
        title = article('h4[class="weui_media_title"]').text()
        url = 'http://mp.weixin.qq.com' + article('h4[class="weui_media_title"]').attr('hrefs')
        summary = article('.weui_media_desc').text()
        date = article('.weui_media_extra_info').text()
        pic = self.parse_cover_pic(article)
        content = self.parse_content_by_url(url).html()
 
        return {
            'title': title,
            'url': url,
            'summary': summary,
            'date': date,
            'pic': pic,
            'content': content
        }
 
    def parse_cover_pic(self, article):
        ' 解析文章封面图片 '
        pic = article('.weui_media_hd').attr('style')
 
        p = re.compile(r'background-image:url\((.*?)\)')
        rs = p.findall(pic)
 
        return rs[0] if len(rs) > 0 else ''
 
    def parse_content_by_url(self, url):
        ' 获取文章详情内容 '
        page_html = self.get_selenium_js_html(url)
        return pq(page_html)('#js_content')
 
    def save_file(self, content):
        ' 数据写入文件 '
        with open(self.kw+'.txt', 'w') as f:
            f.write(content)
            #print(content.decode('utf8'))
 
    def log(self, msg):
        ' 自定义log函数 '
        print (u'%s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg))
 
    def need_verify(self, selenium_html):
        ' 有时候对方会封锁ip，这里做一下判断，检测html中是否包含id=verify_change的标签，有的话，代表被重定向了，提醒过一阵子重试 '
        return pq(selenium_html)('#verify_change').text() != ''
 
 
    def run(self):
        ' 爬虫入口函数 '
 
        # Step 1：GET请求到搜狗微信引擎，以微信公众号英文名称作为查询关键字
        self.log(u'开始获取，微信公众号英文名为：%s' % self.kw)
        self.log(u'开始调用sougou搜索引擎')
        sougou_search_html = self.get_search_result_by_kw()
 
        # Step 2：从搜索结果页中解析出公众号主页链接
        self.log(u'获取sougou_search_html成功，开始抓取公众号对应的主页wx_url')
        wx_url = self.get_wx_url_by_sougou_search_html(sougou_search_html)
        self.log(u'获取wx_url成功，%s' % wx_url)
 
        # Step 3：Selenium+PhantomJs获取js异步加载渲染后的html
        self.log(u'开始调用selenium渲染html')
        selenium_html = self.get_selenium_js_html(wx_url)
 
        # Step 4: 检测目标网站是否进行了封锁
        if self.need_verify(selenium_html):
            self.log(u'爬虫被目标网站封锁，请稍后再试')
        else:
            # Step 5: 使用PyQuery，从Step 3获取的html中解析出公众号文章列表的数据
            self.log(u'调用selenium渲染html完成，开始解析公众号文章')
            articles = self.parse_wx_articles_by_html(selenium_html)
            self.log(u'抓取到微信文章%d篇' % len(articles))
 
            # Step 6: 把微信文章数据封装成字典的list
            self.log(u'开始整合微信文章数据为字典')
            articles_list = self.switch_arctiles_to_list(articles)
 
            # Step 7: 把Step 5的字典list转换为Json
            self.log(u'整合完成，开始转换为json')
            data_json = json.dumps(articles_list)
 
            # Step 8: 写文件
            self.log(u'转换为json完成，开始保存json数据到文件')
            self.save_file(data_json)
 
            self.log(u'保存完成，程序结束')
 
 
 
# main
if __name__ == '__main__':
    #weixin_spider('ArchNotes').run()
    weixin_spider('xiaobingyanjiu').run()
