# -*- coding:utf-8 -*- 
import pandas as pd
import numpy as np
import sys,requests,os
import lxml.html
from lxml import etree
import re,time
from pandas.compat import StringIO
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
#reload(sys)
#sys.setdefaultencoding('utf-8')
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
REPORT_COLS=['code','name','preclose','open','close','high','low','Volumn','Change','p_ch','time']
REPORT_COLS1=['N1','mark','name','pchg','main_buy','main_pnt','sb_buy','sb_pnt','b_buy','b_pnt','m_buy','m_pnt','sm_buy','sm_pnt','name','code']
SH_COLS=['N1','code','name','close','pchg','zl_netinamount','zl_netratio','sb_netinamount','sb_netratio','b_netinamont','b_netratio','m_netinamount','m_netratio','sm_netinamount','sm_netratio','date']
REPORT_usa1=['code','name','preclose','open','close','high','low','volumn','chg','chg_p','amplitude','N1','N2','N3','N4','N5','N6','N7','time','total_shares','markcap']
REPORT_usa2=['preclose','open','close','high','low','volumn','chg','N1','N2','N4','N6','total_shares','markcap']
REPORT_index1=['code','name','preclose','open','close','high','low','chg','chg_p','amplitude','time']
REPORT_index2=['preclose','open','close','high','low','chg','chg_p','amplitude']
TRD_COLS=['symbol','name','trade_hk','pch_hk','code','trade_a','pch_a','Bijia_h/a','Exchange','premium_h/a']
REPORT_hgt=['date','N_O','Buy','Sell','B_S','Day_balance','T_balance','Name','p_change','code','index','index_pchg']
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

def get_currency_data():
    _write_head()
    df =  _get_curr_data(pd.DataFrame())
    if df is not None:
        return df


def _get_curr_data(dataArr):
    _write_console()
    try:
        url='http://hq2gjqh.eastmoney.com/EM_Futures2010NumericApplication/Index.aspx?jsName=fxrc&Type=S&SortType=A&pageSize=2000&page=1&style=28AllRate&_g=0.9714039387626267'
        #print(url)
        r=requests.get(url,timeout=10)
        r=r.text#.decode('gbk','ignore').encode('gbk')
        #print r
        text=r
        r=r.split('={rank:["',1)[1]
        r=r.split('],pages',1)[0]
        r=r.replace('",','\n')
        r=r.replace('"','')
        #print r
        df = pd.read_csv(StringIO(r),header=None,encoding='utf8')
        df=df.drop(0,axis=1)
        df=df.drop(8,axis=1)
        df=df.drop(10,axis=1)
        df=df.drop(11,axis=1)
        df=df.drop(12,axis=1)
        df=df.drop(13,axis=1)
        df=df.drop(14,axis=1)
        df=df.drop(15,axis=1)
        df=df.drop(16,axis=1)
        df=df.drop(19,axis=1)
        df=df.drop(20,axis=1)
        df=df.drop(21,axis=1)
        df=df.drop(22,axis=1)
        df=df.drop(23,axis=1)
        df=df.drop(24,axis=1)
        df=df.drop(25,axis=1)
        df=df.drop(26,axis=1)
        df=df.drop(28,axis=1)
        df.columns=REPORT_COLS
        df['code']=df['code'].astype(str)#map(lambda x:str(x))
        df['time']=pd.to_datetime(df['time'])
        return df
    except Exception as e:
        print(e)

def _handle_cashflow(r):
    r=r.split("data:[",1)[1]
    r=r.replace('var vIlEropE={pages:2,data:[','')
    r=r.replace('var WzYQPLmv={pages:1,data:[','')
    r=r.replace('var uywRInNK={pages:59,date:"2014-10-22",data:[','')
    r=r.replace('var uywRInNK={pages:59,date:"2014-10-22",data:[','')
    r=r.replace('var SVNsQJPa={pages:4,data:[','')
    r=r.replace(']}','')
    r=r.replace('",','\n')
    r=r.replace('"','')
    r=r.replace(',-,','')
    return r

def get_hangye_list():
    Darr=pd.DataFrame()
    try:
        for i in range(1,3,1):
            url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cmd=C._BKHY&type=ct&st=%28BalFlowMain%29&sr=-1&p={0}&ps=50&js=var%20vIlEropE={1}&token=894050c76af8597a853f5b408b759f5d&sty=DCFFITABK&rt=48581414".format(i,'{pages:%28pc%29,data:[%28x%29]}')
            print (url)
            r=requests.get(url)
            r=r.text
            r=_handle_cashflow(r)
            df=pd.read_csv(StringIO(r),header=None)
            Darr=Darr.append(df)

        Darr.columns=REPORT_COLS1
        Darr.drop_duplicates(subset='mark',inplace=True)
        Darr=Darr.sort_values(by='main_buy',ascending=False)
        Darr=Darr.set_index('mark')
        del Darr['N1']
        return Darr
    except Exception as e:
        print(e)
        
def get_diyu_list():
    Darr=pd.DataFrame()
    try:
        for i in range(1,3,1):
            url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cmd=C._BKDY&type=ct&st=%28BalFlowMainNet5%29&sr=-1&p={0}&ps=50&js=var%20WzYQPLmv={1}&token=894050c76af8597a853f5b408b759f5d&sty=DCFFITABK5&rt=48581407".format(i,'{pages:%28pc%29,data:[%28x%29]}')
            print (url)
            r=requests.get(url)
            r=r.text
            r=_handle_cashflow(r)
            df=pd.read_csv(StringIO(r),header=None)
            Darr=Darr.append(df)

        Darr.columns=REPORT_COLS1
        Darr.drop_duplicates(subset='mark',inplace=True)
        Darr=Darr.sort_values(by='main_buy',ascending=False)
        Darr=Darr.set_index('mark')
        del Darr['N1']
        return Darr
    except Exception as e:
        print(e)

def get_gainian_list():
    Darr=pd.DataFrame()
    try:
        for i in range(1,3,1):
            url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?cmd=C._BKGN&type=ct&st=%28BalFlowMain%29&sr=-1&p={0}&ps=50&js=var%20SVNsQJPa={1}&token=894050c76af8597a853f5b408b759f5d&sty=DCFFITABK&rt=48583857".format(i,'{pages:%28pc%29,data:[%28x%29]}')
            print (url)
            r=requests.get(url)
            r=r.text
            r=_handle_cashflow(r)
            df=pd.read_csv(StringIO(r),header=None)
            Darr=Darr.append(df)

        Darr.columns=REPORT_COLS1
        Darr.drop_duplicates(subset='mark',inplace=True)
        Darr=Darr.sort_values(by='main_buy',ascending=False)
        Darr=Darr.set_index('mark')
        del Darr['N1']
        return Darr
    except Exception as e:
        print(e)

def get_all_list():
    Darr=pd.DataFrame()
    try:
        for i in range(1,4,1):
            url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=%28BalFlowMain%29&sr=-1&p={0}&ps=1000&js=var%20uywRInNK={1}&token=894050c76af8597a853f5b408b759f5d&cmd=C._AB&sty=DCFFITA&rt=4858136".format(i,'{pages:%28pc%29,date:%222014-10-22%22,data:[%28x%29]}')
            print (url)
            r=requests.get(url)
            r=r.text
            r=_handle_cashflow(r)
            df=pd.read_csv(StringIO(r),header=None,encoding='utf8')
            Darr=Darr.append(df)
            time.sleep(0.01)
        Darr.columns=SH_COLS
        Darr.drop_duplicates(subset='code',inplace=True)
        Darr['code']=Darr['code'].map(lambda x:str(x).zfill(6))
        Darr=Darr.set_index('code')
        Darr['date']=pd.to_datetime(Darr['date'])
        del Darr['N1']
        return Darr
    except Exception as e:
        print(e)

def _handle_usa(r):
    r=r.split("={rank:[",1)[1]
    r=r.replace('],pages:1}','')
    r=r.replace('",','\n')
    r=r.replace('"','')
    #r=r.decode('gb18030')
    return r

def get_usa_list():
    Darr=pd.DataFrame()
    try:
        for i in range(1,3,1):
            url="http://hq2gjgp.eastmoney.com/EM_Quote2010NumericApplication/Index.aspx?jsName=UsStockJs&dataName=rank&Type=s&style=70&sortType=C&sortRule=-1&page={0}&pageSize=50000&_g=0.297812950635049".format(i)
            print (url)
            r=requests.get(url)
            r=r.text
            r=_handle_usa(r)
            dd=pd.read_csv(StringIO(r),header=None)
            Darr=Darr.append(dd)
        #"""
        Darr=Darr.drop(0,axis=1)
        Darr=Darr.drop(8,axis=1)
        Darr=Darr.drop(12,axis=1)
        Darr=Darr.drop(14,axis=1)
        Darr=Darr.drop(15,axis=1)
        Darr=Darr.drop(16,axis=1)
        Darr=Darr.drop(19,axis=1)
        Darr=Darr.drop(20,axis=1)
        Darr=Darr.drop(26,axis=1)
        Darr=Darr.drop(27,axis=1)
        Darr=Darr.drop(29,axis=1)
        Darr=Darr.drop(32,axis=1)
        #"""
        Darr.columns=REPORT_usa1
        for label in REPORT_usa2:
            Darr[label]=Darr[label].astype(float)
        #print Darr
        for label in ['code','name','time']:
            Darr[label]=Darr[label].astype(str)
        Darr['only']=Darr['code']+Darr['time']
        Darr=Darr.drop_duplicates(subset=['only'])
        del Darr['only']
        return Darr
    except Exception as e:
        print(e)
        
def _handle_index(r):
    r=r.split("quotation:[",1)[1]
    r=r.replace(']}','')
    r=r.replace('",','\n')
    r=r.replace('"','')
    #r=r.decode('gb18030')
    r=r.replace("%",'')
    return r
def _hapd(dd):
    dd=dd.drop(0,axis=1)
    dd=dd.drop(8,axis=1)
    dd=dd.drop(9,axis=1)
    dd=dd.drop(12,axis=1)
    dd=dd.drop(14,axis=1)
    dd=dd.drop(15,axis=1)
    dd=dd.drop(16,axis=1)
    dd=dd.drop(17,axis=1)
    dd=dd.drop(22,axis=1)
    dd=dd.drop(18,axis=1)
    dd=dd.drop(19,axis=1)
    dd=dd.drop(20,axis=1)
    dd=dd.drop(21,axis=1)
    dd=dd.drop(23,axis=1)
    dd=dd.drop(24,axis=1)
    dd=dd.drop(25,axis=1)
    dd=dd.drop(26,axis=1)
    dd=dd.drop(27,axis=1)
    dd=dd.drop(29,axis=1)
    dd=dd.drop(30,axis=1)
    dd=dd.drop(31,axis=1)
    dd=dd.drop(32,axis=1)
    dd.columns=REPORT_index1
    for label in REPORT_index2:
        dd[label]=dd[label].astype(float)
    #print Darr
    for label in ['code','name','time']:
        dd[label]=dd[label].astype(str)
    dd['only']=dd['code']+dd['time']
    dd=dd.drop_duplicates(subset=['only'])
    del dd['only']
    return dd

def get_global_index():
    #Darr=pd.DataFrame()
    try:
        url="http://hq2gjgp.eastmoney.com/EM_Quote2010NumericApplication/Index.aspx?reference=rtj&Type=Z&jsName=quote_global&ids=NKY7,KOSPI7,FSSTI7,TWSE7,SENSEX7,JCI7,VNINDEX7,FBMKLC7,SET7,KSE1007,PCOMP7,CSEALL7,AS517,NZSE50FG7,CASE7,INDU7,SPX7,CCMP7,SPTSX7,MEXBOL7,IBOV7,UKX7,DAX7,CAC7,IBEX7,FTSEMIB7,AEX7,SMI7,OMX7,ICEXI7,ISEQ7,INDEXCF7,ASE7,BEL207,LUXXX7,KFX7,HEX7,OBX7,ATX7,WIG7,PX7"
        print (url)
        r=requests.get(url)
        r=r.text
        r=_handle_index(r)
        dd=pd.read_csv(StringIO(r),header=None,encoding='utf8')
        dd=_hapd(dd)
        dd=dd.set_index('code')
        return dd
    except Exception as e:
        print(e)

def get_mainland_index():
    #Darr=pd.DataFrame()
    try:
        url="http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/Index.aspx?type=z&jsName=quote_hs&reference=rtj&ids=0000011,3990012,0003001,3990052,3990062"
        print (url)
        r=requests.get(url)
        r=r.text
        r=_handle_index(r)
        dd=pd.read_csv(StringIO(r),header=None,encoding='utf8')
        dd=_hapd(dd)
        dd['code']=dd['code'].map(lambda x: str(x).zfill(6))
        dd=dd.set_index('code')
        return dd
    except Exception as e:
        print(e)
def get_hongkong_index():
    #Darr=pd.DataFrame()
    try:
        url="http://hq2hk.eastmoney.com/EM_Quote2010NumericApplication/Index.aspx?reference=rtj&Type=z&jsName=quote_hk&ids=1100005,1100105,1100305,1100505"
        print (url)
        r=requests.get(url)
        r=r.text
        r=_handle_index(r)
        dd=pd.read_csv(StringIO(r),header=None,encoding='utf8')
        dd=_hapd(dd)
        dd=dd.set_index('code')
        return dd
    except Exception as e:
        print(e)

def _handle_hk_ha(r):
    r=r.split("rank:[",1)[1]
    r=r.split(",pages",1)[0]
    r=r.replace('",','\n')
    r=r.replace('"','\n')
    r=r.replace(']','')
    try:
        r=r.encode('utf8')
    except Exception as e:
        print (e)
    return r

def get_ha_trading_data():
    url='http://hqguba1.eastmoney.com/hk_ah/AHQuoteList.aspx?jsName=quote_data1&page=1&pageSize=10000&sortType=7&sortRule=-1&_g=0.33073830841158103'
    r=requests.get(url=url,timeout=10)
    r=r.text
    r=_handle_hk_ha(r)

    df=pd.read_csv(StringIO(r),header=None)
    df.columns=TRD_COLS
    df['symbol']=df['symbol'].map(lambda x: str(x).zfill(5))
    df['code']=df['code'].map(lambda x: str(x).zfill(6))
    df=df.set_index('symbol')
    return df

def _handle_hgt(r):
    r=r.text
    r=r.split("data:[",1)[1]
    r=r.replace(']}','')
    r=r.replace('",','\n')
    r=r.replace('"','')
    dft=pd.read_csv(StringIO(r),header=None,encoding='utf8')
    dft.columns=REPORT_hgt
    dft=dft.set_index('date')
    del dft['N_O']
    return dft

def get_hhist_data():
    try:
        for i in range(1,2,1):
            url="http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=SHT&sty=SHTHPS&st=2&sr=-1&p={0}&ps=30&js=var%20jSKwIjoM={1}&mkt=1&rt=48579990".format(i,'{pages:%28pc%29,data:[%28x%29]}')
            print (url)
            r=requests.get(url)
            df=_handle_hgt(r)
        return df
    except Exception as e:
        print(e)
        
def get_ghist_data():
    try:
        for i in range(1,2,1):
            url="http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=SHT&sty=SHTHPS&st=2&sr=-1&p={0}&ps=30&js=var%20Zqpsgzqk={1}&mkt=2&rt=48579996".format(i,'{pages:%28pc%29,data:[%28x%29]}')
            print (url)
            r=requests.get(url)
            df=_handle_hgt(r)
        return df
    except Exception as e:
        print(e)

def get_hbf_t(date):
    """
    date format like YYYY-MM,string format.
    """
    _write_head()
    DataArr=pd.DataFrame()
    if date[-1]=='6' or date[-1]=='9':
        date=date+'-30'
    else:
        date =date+'-31'
    qf='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=ZLCC&st=2&sr=-1&p=1&ps=50000000&js=var%20sAenYaSr={0}&stat=2&cmd=1&fd={1}&rt=48822247'.format('{pages:%28pc%29,data:[%28x%29]}',date)
    ss='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=ZLCC&st=2&sr=-1&p=1&ps=50000000&js=var%20tjesHrgl={0}&stat=3&cmd=1&fd={1}&rt=48822242'.format('{pages:%28pc%29,data:[%28x%29]}',date)
    qs='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=ZLCC&st=2&sr=-1&p=1&ps=50000000&js=var%20ZmVPrQMu={0}&stat=4&cmd=1&fd={1}&rt=48822240'.format('{pages:%28pc%29,data:[%28x%29]}',date)
    bx='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=ZLCC&st=2&sr=-1&p=1&ps=50000000&js=var%20UPTprWza={0}&stat=5&cmd=1&fd={1}&rt=48822239'.format('{pages:%28pc%29,data:[%28x%29]}',date)
    xt='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=ZLCC&st=2&sr=-1&p=1&ps=50000000&js=var%20GCanMloZ={0}&stat=6&cmd=1&fd={1}&rt=48822237'.format('{pages:%28pc%29,data:[%28x%29]}',date)
    jj='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=ZLCC&st=2&sr=-1&p=1&ps=50000000&js=var%20yhahtDLE={0}&stat=1&cmd=1&fd={1}&rt=48822134'.format('{pages:%28pc%29,data:[%28x%29]}',date)
    lists=[jj,qf,ss,qs,bx,xt]
    t=1
    for i in lists:
        _write_console()
        #print i
        r=requests.get(url=i,timeout=10)
        r=r.text
        r=r.split('data:[',1)[1]
        r=r.replace('",','\n')
        r=r.replace('"','')
        r=r.replace(']}','')
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=['code','name','funds','totals_hbf','tv_hbf/pc_ts','position','ch_amount','ch_percent','date']
        df['ftype']=t
        t=t+1
        DataArr=DataArr.append(df)
    for label in ['totals_hbf','tv_hbf/pc_ts','ch_amount','ch_percent']:
        DataArr[label]=DataArr[label].astype(float)
    DataArr['code']=DataArr['code'].map(lambda x: str(x).zfill(6))
    return DataArr

def get_hbf_d(code,date):
    """
    date like YYYY-MM,string format.
    code is the sharecode listed in shanghai or shenzhen
    """
    if date[-1]=='6' or date[-1]=='9':
        date=date+'-30'
    else:
        date =date+'-31'

    url='http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=ZLSJ&sty=CCJGMX&st=2&sr=-1&p=1&ps=30000000&js=var%20IuLulRvA={0}&stat=0&code={1}&fd={2}&rt=48822187'.format('{pages:%28pc%29,data:[%28x%29]}',code,date)
    r=requests.get(url=url,timeout=10)
    r=r.text
    r=r.split('data:[',1)[1]
    r=r.replace('",','\n')
    r=r.replace('"','')
    r=r.replace(']}','')
    df=pd.read_csv(StringIO(r),header=None)
    df.columns=['code','name','fcode','fname','type','totals_hbf','tv_hbf','percent_total_shares','percent_current_shares','date']
    df['code']=df['code'].map(lambda x: str(x).zfill(6))
    df['fcode']=df['fcode'].map(lambda x: str(x).zfill(6))
    for label in ['totals_hbf','tv_hbf','percent_total_shares','percent_current_shares']:
        df[label]=df[label].astype(float)
    return df
