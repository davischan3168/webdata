# -*- coding:utf-8 -*- 
"""
基本面数据接口 
Created on 2015/01/18
@author: Davis Chan
@group : Davis-webdata
@contact: racheal123@163.com
"""
import pandas as pd
import sys,os,time
import lxml.html
from lxml import etree
import requests,json
import re
from pandas.compat import StringIO
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
reload(sys)
sys.setdefaultencoding('utf-8')
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
TRD_COLS=['symbol','name','engname','tradetype','lasttrade','prevclose','open','high','low','volume','currentvolume','amount','ticktime','buy','sell','high_52week','low_52week','eps','dividend','stocks_sum','pricechange','changepercent']
FR_COLS=['Closing_Date','Current_Ratio_Analysis','Capital_Adequacy_(%)','Cost-to-Income_(%)','Liquid_Fund/Deposits_(%)','Trading_Analysis','Loans/Deposits_(%)','Loans/Equity_(X)','Loans/Total_Assets_(%)','Deposits/Equity_(X)','Deposits/Total_Assets_(%)','Return_on_Investment_Analysis','Return_on_Loans_(%)','Return_on_Deposits_(%)','Return_on_Equity_(%)','Return_on_Total_Assets_(%)','Investment_Income_Analysis','Dividend_Payout_(%)','Related_Statistics','Fiscal_Year_High','Fiscal_Year_Low','Fiscal_Year_PER_Range_High_(X)','Fiscal_Year_PER_Range_Low_(X)','Fiscal_Year_Yield_Range_High_(%)','Fiscal_Year_Yield_Range_Low_(%)']
Div_COls=['Date','Year','Particular','Type','Ex-Date','Book Close Date','Payable Date']
DATA_GETTING_TIPS = '[Getting data:]'
DATA_GETTING_FLAG = '#'
MI={'HSI':'hang-sen-40','DJI':'us-30','SPX':'us-spx-500','IXIC':'nasdaq-composite','GDDAXI':'germany-30','FTSE':'uk-100'}
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
def delect_same_rows(fp):
    print 'update file......'
    if os.path.exists(fp):
        df=pd.read_csv(fp)#,index_col=0)#,encoding='gbk')
        try:
            df=df.drop_duplicates(subset=['Closing Date'])
            df=df.sort_values(by=['Closing Date'])
        except:
            df=df.drop_duplicates(subset=['Date'])
            df=df.sort_values(by=['Date'])
        df=df.set_index('Closing Date')
        df.to_csv(fp)
    return df

def _handle(r):
    r=r.text
    html = lxml.html.parse(StringIO(r))
    res = html.xpath("//table[@id='cnhk-list']/*/tr")
    if PY3:
        sarr = [etree.tostring(node).decode('utf-8') for node in res]
    else:
        sarr = [etree.tostring(node) for node in res]
    sarr = ''.join(sarr)
    sarr = '<table>%s</table>'%sarr
    df = pd.read_html(sarr)[0]
    #print df
    df=df.drop(6,axis=1)
    #df=df.drop('Trend',axis=1)
    return df

def _handle_div(r):
    r=r.text
    html = lxml.html.parse(StringIO(r))
    res = html.xpath("//table[@class='tab05']/*/tr")
    if PY3:
        sarr = [etree.tostring(node).decode('gbk') for node in res]
    else:
        sarr = [etree.tostring(node) for node in res]
    sarr = ''.join(sarr)
    sarr = '<table>%s</table>'%sarr
    df = pd.read_html(sarr)[0]
    df=df.drop(0)
    df=df.drop(2,axis=1)
    return df

def _pre_code(code):
    code=str(code).zfill(5)
    return code

def get_hk_firatio_data_year(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [4]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/financial-ratios?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
        dataArr=dataArr.drop('Trading Analysis',axis=1)
    return dataArr

def get_hk_firatio_data_hyear(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [2]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/financial-ratios?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
        dataArr=dataArr.drop('Trading Analysis',axis=1)
    return dataArr

def get_hk_firatio_data(code):
    df=get_hk_firatio_data_year(code)
    dd=get_hk_firatio_data_hyear(code)
    df=df.append(dd)
    df=df.sort_index()
    df=df.dropna(how='all',axis=0)
    return df

def get_hk_ploss_data_year(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [4]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/profit-loss?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
        #dataArr=dataArr.drop('Trading Analysis',axis=1)
    return dataArr
def get_hk_ploss_data_hyear(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [2]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/profit-loss?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
        #dataArr=dataArr.drop('Trading Analysis',axis=1)
        return dataArr

def get_hk_ploss_data(code):
    df=get_hk_ploss_data_year(code)
    dd= get_hk_ploss_data_hyear(code)
    df=df.append(dd)
    df=df.sort_index()
    df=df.dropna(how='all',axis=0)
    return df

def get_hk_bsheet_data_year(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [4]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/balance-sheet?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
    return dataArr

def get_hk_bsheet_data_hyear(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [2]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/balance-sheet?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
    return dataArr
def get_hk_bsheet_data(code):
    df = get_hk_bsheet_data_year(code)
    dd = get_hk_bsheet_data_hyear(code)
    df=df.append(dd)
    df=df.sort_index()
    df=df.dropna(how='all',axis=0)
    return df

def get_hk_earsummary_data_year(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [4]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/earnings-summary?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0,axis=0)
        dataArr=dataArr.set_index('Closing Date')
    return dataArr

def get_hk_earsummary_data_hyear(code):
    code=_pre_code(code)
    dataArr=pd.DataFrame()
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    for i in [2]:
        url="http://www.aastocks.com/en/stocks/analysis/company-fundamental/earnings-summary?symbol=%s&period=%s"%(code,i)
        r=requests.get(url=url,timeout=10,headers=send_headers)
        df=_handle(r)
        df=df.T
        dataArr=dataArr.append(df)
        uname=dataArr.ix[0,:]
        dataArr.columns=uname
        dataArr=dataArr.drop(0)
        dataArr=dataArr.set_index('Closing Date')
    return dataArr
def get_hk_earsummary_data(code):
    df = get_hk_earsummary_data_year(code)
    dd = get_hk_earsummary_data_hyear(code)
    df=df.append(dd)
    df=df.sort_index()
    df=df.dropna(how='all',axis=0)
    return df

def get_hk_divhis_data(code):
    url="http://stock.finance.sina.com.cn/hkstock/dividends/%s.html"%code
    send_headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding':'gzip, deflate',
                  'Accept-Language':'zh,zh-CN;q=0.5',
                  'Connection':'keep-alive',
                  'DNT':'1',
                  'Host':'www.aastocks.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'}
    r=requests.get(url=url,timeout=10)
    df=_handle_div(r)
    df.columns=Div_COls
    return df

def get_HSI_index():
    _write_console()
    dataArr=pd.DataFrame()
    try:
        url='http://cn.investing.com/indices/hang-sen-40-historical-data'
        #print(url)
        r=requests.get(url)
        r=r.content
        text=r
        text = text.replace('--', '')
        text = text.replace('年','-')
        text = text.replace('月','-')
        text = text.replace('日','')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@id=\"curr_table\"]/tbody/tr")
        if PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        #print sarr
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df=df.drop(0)
        df.columns = ['Date','Close','Open','High','Low','Volumn','Change']
        df.Date=pd.to_datetime(df['Date'])
        #df=df.set_index('Date')
        dataArr = dataArr.append(df, ignore_index=True)
        return dataArr
    except Exception as e:
        print(e)
def get_mainindex_data(code):
    """
    获得全球主要股指指数的数据
    Parameters:
    --------------------
      code:String
    Return
    """

    df =  _get_mainindex_investing(code,pd.DataFrame())
    if df is not None:
        #df['code'] = df['code'].map(lambda x:str(x).zfill(6))
        return df
def _get_mainindex_investing(code,dataArr):
    _write_console()
    try:
        url='http://cn.investing.com/indices/%s-historical-data'%MI[code]
        print(url)
        r=requests.get(url)
        r=r.content
        text=r
        text = text.replace('--', '')
        text = text.replace('年','-')
        text = text.replace('月','-')
        text = text.replace('日','')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@id=\"curr_table\"]/*/tr")
        if PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        print sarr
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        df=df.drop(0)
        df.columns = REPORT_COLS
        dataArr = dataArr.append(df, ignore_index=True)
        return dataArr
    except Exception as e:
        print(e)
