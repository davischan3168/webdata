# -*- coding:utf-8 -*- 
import pandas as pd
import numpy as np
import sys,os,json,time
#from tushare.stock import cons as ct
import lxml.html
from lxml import etree
import re,sys,os,requests
try:
    from io import StringIO
except:
    from pandas.compat import StringIO
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
#reload(sys)
#sys.setdefaultencoding('gbk')
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
REPORT_COLS=['date','N_O','Buy','Sell','B_S','Day_balance','T_balance','Name','p_change','code','index','index_pchg']
Main14_COLS=['date','eps','np','np_yoy','np_d','business_income','bi_yoy','nabs','roe','roe_a','a_libility_r','reservedPerShare','undistrib_ps','cf_ps']
#,'sale_margin','inventory_turnover_rate']
Main16_COLS=['date','eps','np','np_yoy','np_d','business_income','bi_yoy','nabs','roe','roe_a','a_libility_r','reservedPerShare','undistrib_ps','cf_ps','sale_margin','inventory_turnover_rate']
REPORT_cash=['code','name','close','p_change','turnover','inamount','outamount','netamount','t_amount','big_inamount']
Main14_COLShk=['date','eps','eps_d','div','nvps','cfps','bsps','reservedPerShare','profits_0000','roe','mb_np_r','a_libility_r']
DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'
def _check_input(year, quarter):
    if isinstance(year, str) or year < 1989 :
        raise TypeError(DATE_CHK_MSG)
    elif quarter is None or isinstance(quarter, str) or quarter not in [1, 2, 3, 4]:
        raise TypeError(DATE_CHK_Q_MSG)
    else:
        return True
def _write_head():
    sys.stdout.write(DATA_GETTING_TIPS)
    sys.stdout.flush()

def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()
PY3 = (sys.version_info[0] >= 3)



def get_current_hu_ths():
    _write_head()
    _write_console()
    try:
        url='http://data.10jqka.com.cn/hgt/hgtb/'
        r=requests.get(url)
        r=r.text
        r=r.split('var dataDay = [[[',1)[1]
        #r=r.split('["2016-04-12",1731.5500]]];',1)[0]
        r=r.split(']]];',1)[0]
        r=r.split(']],[[',1)[0]
        r=r.replace('],','\n')
        r=r.replace('[','')
        r=r.replace('"','')
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=['time','trade_amount','day_balance']
        return df
    except Exception as e:
        print(e)    
def get_current_hongk_ths():
    _write_head()
    _write_console()
    try:
        url='http://data.10jqka.com.cn/hgt/ggtb/'
        r=requests.get(url)
        r=r.text
        r=r.split('var dataDay = [[[',1)[1]
        #r=r.split('["2016-04-12",1731.5500]]];',1)[0]
        r=r.split(']]];',1)[0]
        r=r.split(']],[[',1)[0]
        r=r.replace('],','\n')
        r=r.replace('[','')
        r=r.replace('"','')
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=['time','trade_amount','day_balance']
        return df
    except Exception as e:
        print(e)    
def _handle(r):
    r=r.replace('[','')
    r=r.replace(']','')
    r=r.replace('}','')
    r=r.replace('simple','')
    r=r.replace('title','')
    r=r.replace('year','')
    r=r.replace(':','')
    r=r.replace('"','')
    r=r.replace('false','')
    return r
def _filter_data_fi(r):
    r=r.text
    r=r.split('"report":',1)[1]
    r=r.split(']]}',1)[0]
    r=r.replace('],','\n')
    f=r.split(':[[',2)[0]
    q=r.split(':[[',2)[1]
    y=r.split(':[[',2)[2]
    f=_handle(f)
    q=_handle(q)
    y=_handle(y)
    return f,q,y

def get_finance_index_ths(code):
    _write_head()
    _write_console()
    try:
        url="http://stockpage.10jqka.com.cn/basic/%s/main.txt"%code
        r=requests.get(url,timeout=10)
        f,q,y=_filter_data_fi(r)
        df=pd.read_csv(StringIO(f),header=None)
        df=df.T
        if df.shape[1]==14:
            df.columns=Main14_COLS
            df['sale_margin']=np.nan
            df['inventory_turnover_rate']=np.nan
        elif df.shape[1]==16:
            df.columns=Main16_COLS
        df['code']=code
        df=df.set_index('code')
        return df
    except Exception as e:
        print(e)

def get_finance_index_simple(code):
    _write_head()
    _write_console()
    try:
        url="http://stockpage.10jqka.com.cn/basic/%s/main.txt"%code
        r=requests.get(url,timeout=10)
        f,q,y=_filter_data_fi(r)
        df=pd.read_csv(StringIO(q),header=None)
        df=df.T
        if df.shape[1]==14:
            df.columns=Main14_COLS
            df['sale_margin']=np.nan
            df['inventory_turnover_rate']=np.nan
        elif df.shape[1]==16:
            df.columns=Main16_COLS
        df['code']=code
        df=df.set_index('code')
        return df
    except Exception as e:
        print(e)

def get_finance_index_year(code):
    _write_head()
    _write_console()
    try:
        url="http://stockpage.10jqka.com.cn/basic/%s/main.txt"%code
        r=requests.get(url,timeout=10)
        f,q,y=_filter_data_fi(r)
        df=pd.read_csv(StringIO(y),header=None)
        df=df.T
        if df.shape[1]==14:
            df.columns=Main14_COLS
            df['sale_margin']=np.nan
            df['inventory_turnover_rate']=np.nan
        elif df.shape[1]==16:
            df.columns=Main16_COLS
        df['code']=code
        df=df.set_index('code')
        return df
    except Exception as e:
        print(e)

def get_cashflow_thsnow():
    """
    Parameters:
    ---------------------------------
    return:
          DataFrame:
             code:      股票代码
             name：     股票名称
             close：    最新价格（元）
             p_change： 涨跌幅%
             turnover： 换手率
             inamount： 流入金额（万元）
             outamount：流出金额（万元）
             netamount：现金净流入额（万元）
             t_amount： 成交金额（万元）
             big_inamount：大胆流入额（万元）
    """    
    _write_head()
    dataArr=pd.DataFrame()
    for i in range(1,55,1):
        try:
            _write_console()
            url="http://data.10jqka.com.cn/funds/ggzjl/field/zdf/order/desc/page/{0}/ajax/1/".format(i)
            send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Encoding':'gzip, deflate',
                      'Accept-Language':'zh,zh-CN;q=0.5',
                      'Connection':'keep-alive',
                      'DNT':'1',
                      'Host':'data.10jqka.com.cn',
                      'Referer':'http://www.10jqka.com.cn/',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            }
            #print(url)
            #print ("Get page %s completed"%i)
            r=requests.get(url,headers=send_headers,timeout=10)
            r=r.text
            text=r
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table/tbody/tr")
            if PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            #print sarr
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(sarr)[0]
            #df=df.drop(0)
            df = df.drop(0, axis=1)
            df.columns = REPORT_cash
            dataArr = dataArr.append(df, ignore_index=True)
        except Exception as e:
            print(e)
    dataArr['code'] = dataArr['code'].map(lambda x:str(x).zfill(6))
    dataArr=dataArr.set_index('code')
    for label in ['p_change','turnover','inamount','outamount','netamount','t_amount','big_inamount']:
        dataArr[label]=dataArr[label].map(lambda x: _str2fl(x))
    return dataArr

def get_cashflow_ths3days():
    """
    Parameters:
    ---------------------------------
    return:
          DataFrame:    
             code:              股票代码
             name:              股票名称
             price:             最新价
             percent_period:    阶段涨跌幅%
             turn_over:         连续换手率%
             net_income:        资金流入净额(万元)
    """    
    _write_head()
    dataArr=pd.DataFrame()
    for i in range(1,55,1):
        try:
            _write_console()
            url="http://data.10jqka.com.cn/funds/ggzjl/board/3/field/zdf/order/desc/page/{0}/ajax/1/".format(i)
            send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Encoding':'gzip, deflate',
                      'Accept-Language':'zh,zh-CN;q=0.5',
                      'Connection':'keep-alive',
                      'DNT':'1',
                      'Host':'data.10jqka.com.cn',
                      'Referer':'http://www.10jqka.com.cn/',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            }
            r=requests.get(url,headers=send_headers,timeout=10)
            r=r.text
            text=r
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table/tbody/tr")
            if PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(sarr)[0]
            df = df.drop(0, axis=1)
            df.columns = ['code','name','price','percent_period','turn_over','net_income']
            dataArr = dataArr.append(df, ignore_index=True)
        except Exception as e:
            print(e)
    dataArr['code'] = dataArr['code'].map(lambda x:str(x).zfill(6))
    dataArr=dataArr.set_index('code')
    for label in ['percent_period','turn_over','net_income']:
        dataArr[label]=dataArr[label].map(lambda x: _str2fl(x))
    return dataArr

def get_cashflow_ths5days():
    """
    Parameters:
    ---------------------------------
    return:
          DataFrame:    
             code:              股票代码
             name:              股票名称
             price:             最新价
             percent_period:    阶段涨跌幅%
             turn_over:         连续换手率%
             net_income:        资金流入净额(万元)
    """    
    _write_head()
    dataArr=pd.DataFrame()
    for i in range(1,55,1):
        try:
            _write_console()
            url="http://data.10jqka.com.cn/funds/ggzjl/board/5/field/zdf/order/desc/page/{0}/ajax/1/".format(i)
            send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Encoding':'gzip, deflate',
                      'Accept-Language':'zh,zh-CN;q=0.5',
                      'Connection':'keep-alive',
                      'DNT':'1',
                      'Host':'data.10jqka.com.cn',
                      'Referer':'http://www.10jqka.com.cn/',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            }
            r=requests.get(url,headers=send_headers,timeout=10)
            r=r.text
            text=r
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table/tbody/tr")
            if PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(sarr)[0]
            df = df.drop(0, axis=1)
            df.columns = ['code','name','price','percent_period','turn_over','net_income']
            dataArr = dataArr.append(df, ignore_index=True)
        except Exception as e:
            print(e)
    dataArr['code'] = dataArr['code'].map(lambda x:str(x).zfill(6))
    dataArr=dataArr.set_index('code')
    for label in ['percent_period','turn_over','net_income']:
        dataArr[label]=dataArr[label].map(lambda x: _str2fl(x))
    return dataArr

def get_cashflow_ths10days():
    """
    Parameters:
    ---------------------------------
    return:
          DataFrame:    
             code:              股票代码
             name:              股票名称
             price:             最新价
             percent_period:    阶段涨跌幅%
             turn_over:         连续换手率%
             net_income:        资金流入净额(万元)
    """    
    _write_head()
    dataArr=pd.DataFrame()
    for i in range(1,55,1):
        try:
            _write_console()
            url="http://data.10jqka.com.cn/funds/ggzjl/board/10/field/zdf/order/desc/page/{0}/ajax/1/".format(i)
            send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Encoding':'gzip, deflate',
                      'Accept-Language':'zh,zh-CN;q=0.5',
                      'Connection':'keep-alive',
                      'DNT':'1',
                      'Host':'data.10jqka.com.cn',
                      'Referer':'http://www.10jqka.com.cn/',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            }
            r=requests.get(url,headers=send_headers,timeout=10)
            r=r.text
            text=r
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table/tbody/tr")
            if PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(sarr)[0]
            df = df.drop(0, axis=1)
            df.columns = ['code','name','price','percent_period','turn_over','net_income']
            dataArr = dataArr.append(df, ignore_index=True)
        except Exception as e:
            print(e)
    dataArr['code'] = dataArr['code'].map(lambda x:str(x).zfill(6))
    dataArr=dataArr.set_index('code')
    for label in ['percent_period','turn_over','net_income']:
        dataArr[label]=dataArr[label].map(lambda x: _str2fl(x))
    return dataArr

def get_cashflow_ths20days():
    """
    Parameters:
    ---------------------------------
    return:
          DataFrame:    
             code:              股票代码
             name:              股票名称
             price:             最新价
             percent_period:    阶段涨跌幅%
             turn_over:         连续换手率%
             net_income:        资金流入净额(万元)
    """    
    _write_head()
    dataArr=pd.DataFrame()
    for i in range(1,55,1):
        try:
            _write_console()
            url="http://data.10jqka.com.cn/funds/ggzjl/board/20/field/zdf/order/desc/page/{0}/ajax/1/".format(i)
            send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Encoding':'gzip, deflate',
                      'Accept-Language':'zh,zh-CN;q=0.5',
                      'Connection':'keep-alive',
                      'DNT':'1',
                      'Host':'data.10jqka.com.cn',
                      'Referer':'http://www.10jqka.com.cn/',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
            }
            r=requests.get(url,headers=send_headers,timeout=10)
            r=r.text
            text=r
            html = lxml.html.parse(StringIO(text))
            res = html.xpath("//table/tbody/tr")
            if PY3:
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
            else:
                sarr = [etree.tostring(node) for node in res]
            sarr = ''.join(sarr)
            sarr = '<table>%s</table>'%sarr
            df = pd.read_html(sarr)[0]
            df = df.drop(0, axis=1)
            df.columns = ['code','name','price','percent_period','turn_over','net_income']
            dataArr = dataArr.append(df, ignore_index=True)
        except Exception as e:
            print(e)
    dataArr['code'] = dataArr['code'].map(lambda x:str(x).zfill(6))
    dataArr=dataArr.set_index('code')
    for label in ['percent_period','turn_over','net_income']:
        dataArr[label]=dataArr[label].map(lambda x: _str2fl(x))
    return dataArr
            
def _filter_hk_data(r):
    r=r.text
    r=r.split('"report":',1)[1]
    r=r.split(']],"year"',1)[0]
    r=r.replace('],','\n')
    r=r.replace('[','')
    r=r.replace(']','')
    r=r.replace('}','')
    r=r.replace('"','')
    r=r.replace('false','')
    return r

def _filter_hk_data1(r):
    r=r.text
    r=r.split(']],"year"',1)[1]
    r=r.replace('],','\n')
    r=r.replace('[','')
    r=r.replace(']','')
    r=r.replace('}','')
    r=r.replace('"','')
    r=r.replace(':','')
    r=r.replace('false','')
    return r

def get_hk_financial_ths(code):
    """
    code like XXXX
    """
    _write_head()
    _write_console()
    try:
        url="http://stockpage.10jqka.com.cn/financeflash/hk/HK%s/keyindex.txt"%code
        r=requests.get(url,timeout=10)
        u=r
        #print url
        r=_filter_hk_data(r)
        df=pd.read_csv(StringIO(r),header=None)
        df=df.T
        df.columns=Main14_COLShk
        df['code']=code
        df=df.set_index('code')
        return df
    except Exception as e:
        print(e)

def get_hk_financial_year(code):
    _write_head()
    _write_console()
    try:
        url="http://stockpage.10jqka.com.cn/financeflash/hk/HK%s/keyindex.txt"%code
        r=requests.get(url,timeout=10)
        u=r
        #print url
        u=_filter_hk_data1(u)
        dfy=pd.read_csv(StringIO(u),header=None)
        dfy=dfy.T
        dfy.columns=Main14_COLShk
        dfy['code']=code
        dfy=dfy.set_index('code')
        return dfy
    except Exception as e:
        print(e)

def _str2fl(x):
    if '万' in x:
        x=x.strip().replace('万','')
        x=float(x)
    elif '亿' in x:
        x=x.strip().replace('亿','')
        x=float(x)*10000
    elif '%' in x:
        x=x.strip().replace('%','')
        x=float(x)
    elif '千' in x:
        x=x.strip().replace('千','')
        x=float(x)/10
    elif x.strip()=='-':
        x=x.strip().replace('-','')
    else:
        pass
    return x
