# -*- coding:utf-8 -*- 
import pandas as pd
import numpy as np
import sys,os
import lxml.html
from lxml import etree
import requests,json
import re
import time
import datetime
today=time.strftime('%Y-%m-%d')
from pandas.compat import StringIO
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
reload(sys)
sys.setdefaultencoding('utf8')
DATE_CHK_MSG = '年度输入错误：请输入1989年以后的年份数字，格式：YYYY'
DATE_CHK_Q_MSG = '季度输入错误：请输入1、2、3或4数字'
REPORT_COLS=['symbol','code','name','trade','pricechange','changepercent','buy','sell','settlement','open','high','low','volume','amount','ticktime','pe',"pe_ttm","nta","pb","mktcap","nmc","turnoverratio"]
HY_COLS=['cate_type','category','name','avg_price','avg_changeratio','turnover','inamount','outamount','netamount','ratioamount','ts_symbol','ts_name','ts_trade','ts_changeratio','ts_ratioamount']
SH_COLS=['symbol','name','trade','changeratio','turnover','amount','inamount','outamount','netamount','ratioamount','r0_in','r0_out','r0_net','r3_in','r3_out','r3_net','r0_ratio','r3_ratio','r0x_ratio']
SH_COLSper=['opendate','trade','changeratio','turnover','netamount','ratioamount','r0_net','r0_ratio','r0x_ratio','cnt_r0x_ratio','cate_ra','cate_na']
TRD_COLShk=['symbol','name','engname','tradetype','lasttrade','prevclose','open','high','low','volume','currentvolume','amount','ticktime','buy','sell','high_52week','low_52week','eps','dividend','stocks_sum','pricechange','changepercent']
TRD_COLSkzz=['symbol','name','trade','pricechange','changepercent','buy','sell','settlement','open','high','low','volume','amount','code','ticktime']
TRD_COLShkha=['symbol','name','trade_hk','pch_hk','code','trade_a','pch_a','Bijia_h/a','Exchange','premium_h/a']
TRD_COLShkhy=['id','industryName','sector_code','companyNumber','risePercent','risePrice','averagePrice:','totalAmount','totalMoney','lz_symbol','lz_Name','lz_risePrice','lz_newprice','lz_risePercent','ld_symbol','ld_Name','ld_risePrice','ld_newprice','ld_risePercent','createTime']
TRD_COLShcg=['symbol','name','engname','tradetype','lasttrade','prevclose','open','high','low','volume','currentvolume','amount','ticktime','buy','sell','high_52week','low_52week','eps','dividend','stocks_sum','pricechange','changepercent']
TRD_COLSgqg=['symbol','name','engname','tradetype','lasttrade','prevclose','open','high','low','volume','currentvolume','amount','ticktime','buy','sell','high_52week','low_52week','eps','dividend','stocks_sum','pricechange','changepercent']
week_COLS=['symbol','name','close','volume','amount','turnover','changes','high','low','open','aov','tag',"day"]
Ind_COLS=['Date','EPS_D','EPS_W','EPS_ad','EPS_a_deducted','NAPS_b_ad','NAPS_a_ad','CFPS',
             'CRPS','UPS','NASPS_D','ROPTA','ROBP','RONP_TA','ROP_C','ROB',
             'ROB_C','ROP_S','ROEquity','ROShare','ROE_S','ROS_gross','ROC3','Percent_non_main',
             'P_BProfit','R_Dispa','ROI','BProfit','ROE','ROE_W','ROE_D','R_Income_I',
             'NP_YOY','NA_YOY','TA_YOY','AC_R_TR','AC_R_TD','I_TD','I_TR','FA_TR',
             'TA_TR','TA_TD','CA_TR','CA_TD','EQ_TR','Current_R','Q_R','Cash_R',
             'I_Pay_T','long_short_R','Eq_R','L_debt_R','R_EQ_FA','R_Debt_EQ','R_L_Asset_Cash','R_Capitalised',
             'TA_Net_R','R_Nt_Book','A_Fix_R','Capital_equity_ratio','liquidation_value_ratio',
             'fixed_assets_ratio','A_L_R','T_A','CF_Sale_R','CFOA_R','CF_PRO_R','CF_L_R','S_INV_Share',
             'S_INV_Bond','S_Operate_INV','L_INV_Share','L_INV_Bond','S_Operate_INV','AR_IN_1','AR_BE_12',
             'AR_BE_23','AR_IN_3','Pay_IN_1','Pay_BE_12','Pay_BE_23','Pay_IN_3','RO_IN_1',
             'OR_BE_12','RO_BE_23','RO_IN_3']
DA_COLS=['EPS_D','EPS_W','EPS_ad','EPS_a_deducted','NAPS_b_ad','NAPS_a_ad','CFPS',
             'CRPS','UPS','NASPS_D','ROPTA','ROBP','RONP_TA','ROP_C','ROB',
             'ROB_C','ROP_S','ROEquity','ROShare','ROE_S','ROS_gross','ROC3','Percent_non_main',
             'P_BProfit','R_Dispa','ROI','BProfit','ROE','ROE_W','ROE_D','R_Income_I',
             'NP_YOY','NA_YOY','TA_YOY','AC_R_TR','AC_R_TD','I_TD','I_TR','FA_TR',
             'TA_TR','TA_TD','CA_TR','CA_TD','EQ_TR','Current_R','Q_R','Cash_R',
             'I_Pay_T','long_short_R','Eq_R','L_debt_R','R_EQ_FA','R_Debt_EQ','R_L_Asset_Cash','R_Capitalised',
             'TA_Net_R','R_Nt_Book','A_Fix_R','Capital_equity_ratio','liquidation_value_ratio',
             'fixed_assets_ratio','A_L_R','T_A','CF_Sale_R','CFOA_R','CF_PRO_R','CF_L_R','S_INV_Share',
             'S_INV_Bond','S_Operate_INV','L_INV_Share','L_INV_Bond','S_Operate_INV','AR_IN_1','AR_BE_12',
             'AR_BE_23','AR_IN_3','Pay_IN_1','Pay_BE_12','Pay_BE_23','Pay_IN_3','RO_IN_1',
             'OR_BE_12','RO_BE_23','RO_IN_3']
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

def _handle(r):
    r=r.split("['yl3d4qagkRhWInMj']",1)[1]
    r=r.replace('([','')
    r=r.replace('])','')
    r=r.replace('},','}\n')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace('symbol','')
    r=r.replace('code','')
    r=r.replace('name','')
    r=r.replace('trade','')
    r=r.replace('pricechange','')
    r=r.replace('changepercent','')
    r=r.replace('buy','')
    r=r.replace('sell','')
    r=r.replace('settlement','')
    r=r.replace('open','')
    r=r.replace('high','')
    r=r.replace('low','')
    r=r.replace('volume','')
    r=r.replace('amount','')
    r=r.replace('ticktime','')
    r=r.replace('per','')
    r=r.replace('per_d','')
    r=r.replace('nta','')
    r=r.replace('pb','')
    r=r.replace('mktcap','')
    r=r.replace('nmc','')
    r=r.replace('turnoverratio','')
    r=r.replace(':','')
    r=r.replace('_d','')
    r=r.replace('null','')
    try:
        r.encode('gb18030')
    except Exception as e:
        print e
    return r

def get_sina_pepb():
    url = "http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList%5B'yl3d4qagkRhWInMj'%5D/Market_Center.getHQNodeDataNew?page=1&num=5000&sort=per_d&asc=0&node=hs_a#"
    r = requests.get(url=url,timeout=10)
    #print url
    r=r.text
    r=_handle(r)
    df=pd.read_csv(StringIO(r),header=None)
    df.columns=REPORT_COLS
    df['ticktime']=pd.to_datetime(df['ticktime'])
    df=df.drop_duplicates(subset='code')
    df['code']=df['code'].map(lambda x:str(x).zfill(6))
    df=df.set_index('code')
    return df
def _handle_bk(r):
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace('cate_type','')
    r=r.replace('category','')
    r=r.replace('ts_name','')
    r=r.replace('name','')
    r=r.replace('avg_price','')
    r=r.replace('avg_changeratio','')
    r=r.replace('turnover','')
    r=r.replace('inamount','')
    r=r.replace('outamount','')
    r=r.replace('netamount','')
    r=r.replace('ratioamount','')
    r=r.replace('ts_symbol','')
    r=r.replace('ts_trade','')
    r=r.replace('ts_changeratio','')
    r=r.replace('ts_ratioamount','')
    r=r.replace('ts_','')
    r=r.replace(':','')
    r=r.replace(r'[','')
    """
    try:
        r=r.encode('gb18030')
    except Exception as e:
        print e
    """
    return r
def get_hangye_sina():
    """
          获得按行业的资金流入流出情况
    ----------
    Return
         
    """
    dataArr=pd.DataFrame()
    for i in xrange(1,4,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_bk?page={0}&num=20&sort=netamount&asc=0&fenlei=0".format(i)
        r=requests.get(url=url)
        r=r.text
        r=_handle_bk(r)
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=HY_COLS
        dataArr=dataArr.append(df)
    dataArr=dataArr.set_index('category')
    return dataArr

def get_gainian_sina():
    """
       获得按概念的资金流入流出情况
    ------------
    Return:
          
    """
    dataArr=pd.DataFrame()
    for i in xrange(1,4,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_bk?page={0}&num=20&sort=netamount&asc=0&fenlei=1".format(i)
        r=requests.get(url=url)
        r=r.text
        r=_handle_bk(r)
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=HY_COLS
        dataArr=dataArr.append(df)
    dataArr=dataArr.set_index('category')
    return dataArr

def get_zjh_sina():
    """
    获得按证监会分类的资金流入流出
    ---------------
    Return
    """
    dataArr=pd.DataFrame()
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_bk?page={0}&num=20&sort=netamount&asc=0&fenlei=2".format(i)
        r=requests.get(url=url)
        r=r.text
        r=_handle_bk(r)
        df=pd.read_csv(StringIO(r),header=None)
        #print df
        #df=df.drop(0,axis=1)
        #print HY_COLS
        df.columns=HY_COLS
        dataArr=dataArr.append(df)
    dataArr=dataArr.set_index('category')
    return dataArr
def _handle_cash(r):
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace(r'r0_in','')
    r=r.replace('in','')
    r=r.replace(r'r0_out','')
    r=r.replace('out','')
    r=r.replace(r'r0_net','')
    r=r.replace('net','')
    r=r.replace(r'r3_in','')
    r=r.replace(r'r3_out','')
    r=r.replace(r'r3_net','')
    r=r.replace('r0_ratio','')
    r=r.replace('r3_ratio','')
    r=r.replace('r0x_ratio','')
    r=r.replace('ratio','')
    r=r.replace('symbol','')
    r=r.replace('name','')
    r=r.replace('trade','')
    r=r.replace('changeratio','')
    r=r.replace('turnover','')
    r=r.replace('amount','')
    r=r.replace('inamount','')
    r=r.replace('outamount','')
    r=r.replace('netamount','')
    r=r.replace('ratioamount','')
    r=r.replace('change','')
    r=r.replace(':','')
    r=r.replace('r3_','')
    r=r.replace(r'[','')
    r=r.replace(r'null','')
    """
    try:
        r=r.encode('gb18030')
    except:
        print "Encode failed"
    """
    return r

def get_share_all_sina():
    """
    获得所有个股的资金流情况
    ------------
    Return
    """
    dataArr=pd.DataFrame()
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_ssggzj?page={}&num=50000&sort=netamount&asc=0&bankuai=&shichang=".format(i)
        #print url
        r=requests.get(url=url)
        r=r.text
        r=_handle_cash(r)
        #r=r.decode('gbk','ignore').encode('gbk')
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=SH_COLS
        dataArr=dataArr.append(df)
        #print dataArr
    dataArr.drop_duplicates(subset=['symbol'],inplace=True)
    dataArr=dataArr.set_index('symbol')
    dataArr['changeratio']=dataArr['changeratio']*100
    dataArr['turnover']=dataArr['turnover']/100
    dataArr['name']=dataArr['name'].astype(str)
    dataArr['name']=dataArr['name'].str.decode('utf8')
    return dataArr
def _handle_cash_per(r):
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace('cnt_r0x_ratio','')
    r=r.replace('opendate','')
    r=r.replace('trade','')
    r=r.replace('changeratio','')
    r=r.replace('turnover','')
    r=r.replace('netamount','')
    r=r.replace('ratioamount','')
    r=r.replace('r0_net','')
    r=r.replace('r0_ratio','')
    r=r.replace('cnt_r0x_ratio','')
    r=r.replace('r0x_ratio','')
    r=r.replace('cate_ra','')
    r=r.replace('cate_na','')
    r=r.replace(':','')
    r=r.replace(r'[','')
    r=r.replace('null','')
    """
    try:
        r=r.encode('gb18030')
    except:
        print "Encode failed"
    """
    return r
def get_share_percode_sina(code):
    """
       获得个股的资金流情况
    -----------------
    Return
    """
    if code[0]=='6':
        code='sh'+code
    else:
        code='sz'+code
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_qsfx_zjlrqs?page=1&num=20000&sort=opendate&asc=0&daima=%s"%code
        r=requests.get(url=url)
        r=r.text
        r=_handle_cash_per(r)
        df=pd.read_csv(StringIO(r),header=None,encoding='gbk')
        df.columns=SH_COLSper
        df['opendate']=pd.to_datetime(df['opendate'])
        df.drop_duplicates(subset=['opendate'],inplace=True)
        df=df.sort_values(by='opendate')
        df=df.set_index('opendate')
        df['changeratio']=df['changeratio']*100
        df['turnover']=df['turnover']/100
        df['code']=code
    return df
def _handle_hk(r):
    r=r.replace('changepercent','')
    r=r.replace('symbol','')
    r=r.replace('engname','') 
    r=r.replace('name','') 
    r=r.replace('tradetype','')
    r=r.replace('lasttrade','') 
    r=r.replace('prevclose','') 
    r=r.replace('high_52week','') 
    r=r.replace('low_52week','') 
    r=r.replace('open','') 
    r=r.replace('high','') 
    r=r.replace('low','') 
    r=r.replace('currentvolume','') 
    r=r.replace('volume','') 
    r=r.replace('amount','') 
    r=r.replace('ticktime','') 
    r=r.replace('buy','') 
    r=r.replace('sell','') 
    r=r.replace('eps','') 
    r=r.replace('dividend','') 
    r=r.replace('stocks_sum','') 
    r=r.replace('pricechange','') 
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace(':','')
    r=r.replace(r'[','')
    """
    try:
        r=r.encode('utf8')
    except Exception as e:
        print e
    """
    return r

def get_hk_trading_sina():
    """
       获得所有港股交易数据
    -------------------
    Return
    """
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page=1&num=40000&sort=symbol&asc=1&node=qbgg_hk&_s_r_a=page"
        r=requests.get(url=url,timeout=10)
        r=r.text
        r=_handle_hk(r)
        df=pd.read_csv(StringIO(r),header=0)
        df.columns=TRD_COLShk
        df['ticktime']=pd.to_datetime(df['ticktime'])
        df['symbol']=df['symbol'].map(lambda x: str(x).zfill(5))
        df=df.set_index('symbol')
    return df
def _handle_kzz(r):
    r=r.replace('changepercent','')
    r=r.replace('symbol','')
    r=r.replace('name','') 
    r=r.replace('open','') 
    r=r.replace('high','') 
    r=r.replace('low','') 
    r=r.replace('volume','') 
    r=r.replace('amount','') 
    r=r.replace('ticktime','') 
    r=r.replace('buy','')
    r=r.replace('trade','')
    r=r.replace('sell','') 
    r=r.replace('settlement','') 
    r=r.replace('code','') 
    r=r.replace('pricechange','') 
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('[','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=re.sub('(?<=\d):','-',r)
    r=r.replace(':','')
    r=r.replace('"','')
    return r



def get_kzz_trading_sina():
    """
    交易所上市的可转债交易数据
    -----------
    Return
    """
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeDataSimple?page=1&num=40000&sort=symbol&asc=1&node=hskzz_z&_s_r_a=init"
        r=requests.get(url=url,timeout=10)
        r=r.text
        r=_handle_kzz(r)

        df=pd.read_csv(StringIO(r),header=None)
        df.columns=TRD_COLSkzz
        #df['ticktime']=pd.to_datetime(df['ticktime'])
        df['symbol']=df['symbol'].map(lambda x: str(x).zfill(5))
        df=df.set_index('symbol')
    return df

def _handle_hk_ha(r):
    r=r.split("rank:[",1)[1]
    r=r.split(",pages",1)[0]
    r=r.replace('",','\n')
    r=r.replace('"','\n')
    r=r.replace(']','')
    return r

def get_hk_ha_trading_sina():
    """
    获得A+H股的交易数据
    -----------
    Return
    """
    url='http://hqguba1.eastmoney.com/hk_ah/AHQuoteList.aspx?jsName=quote_data1&page=1&pageSize=10000&sortType=7&sortRule=-1&_g=0.33073830841158103'
    r=requests.get(url=url,timeout=10)
    r=r.text
    r=_handle_hk_ha(r)
    df=pd.read_csv(StringIO(r),header=None)
    df.columns=TRD_COLShkha
    df['symbol']=df['symbol'].map(lambda x: str(x).zfill(5))
    df['code']=df['code'].map(lambda x: str(x).zfill(6))
    df=df.set_index('symbol')
    return df
def _handle_hk_hy(r):
    r=r.split("hshy=([",1)[1]
    r=r.split("}])",1)[0]
    r=r.replace('},','\n')
    r=r.replace('{','')
    r=r.replace('"','')
    r=r.replace('id','')
    r=r.replace('industryName','')
    r=r.replace('sector_code','')
    r=r.replace('companyNumber','')
    r=r.replace('risePercent','')
    r=r.replace('risePrice','')
    r=r.replace('averagePrice:','')
    r=r.replace('totalAmount','')
    r=r.replace('totalMoney','')
    r=r.replace('lz_symbol','')
    r=r.replace('lz_Name','')
    r=r.replace('lz_risePrice','')
    r=r.replace('lz_newprice','')
    r=r.replace('lz_risePercent','')
    r=r.replace('ld_symbol','')
    r=r.replace('ld_Name','')
    r=r.replace('ld_risePrice','')
    r=r.replace('ld_newprice','')
    r=r.replace('ld_risePercent','')
    r=r.replace('createTime','')
    r=r.replace("lz_",'')
    r=r.replace("ld_",'')
    r=r.replace(":",'')
    #r=r.replace(']','')
    try:
        r=r.encode('gb18030')
    except Exception as e:
        print e
    return r

def get_hk_hangye_trading_sina():
    """
    港股按行业分类的交易数据
    -----------------
    Return
    """
    url='http://stock.finance.sina.com.cn/hshy/api/jsonp.php/var%20hshy=/IndexService.getIndustryInfo?1458696423192'
    r=requests.get(url=url,timeout=10)
    r=r.text
    r=_handle_hk_hy(r)

    df=pd.read_csv(StringIO(r),header=None,encoding='gb18030')
    df.columns=TRD_COLShkhy
    df['id']=df['id'].map(lambda x: str(x).zfill(5))
    df['lz_symbol']=df['lz_symbol'].map(lambda x: str(x).zfill(5))
    df=df.set_index('id')
    return df

def _handle_hk_hcg(r):
    r=r.replace('changepercent','')
    r=r.replace('symbol','')
    r=r.replace('engname','') 
    r=r.replace('name','') 
    r=r.replace('tradetype','')
    r=r.replace('lasttrade','') 
    r=r.replace('prevclose','') 
    r=r.replace('high_52week','') 
    r=r.replace('low_52week','') 
    r=r.replace('open','') 
    r=r.replace('high','') 
    r=r.replace('low','') 
    r=r.replace('currentvolume','') 
    r=r.replace('volume','') 
    r=r.replace('amount','') 
    r=r.replace('ticktime','') 
    r=r.replace('buy','') 
    r=r.replace('sell','') 
    r=r.replace('eps','') 
    r=r.replace('dividend','') 
    r=r.replace('stocks_sum','') 
    r=r.replace('pricechange','') 
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace(':','')
    r=r.replace(r'[','')
    return r
def get_hk_hcg_trading_sina():
    """
    获得红筹股交易数据
    ---------------
    Return
    """
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page=1&num=40000&sort=symbol&asc=1&node=hcg_hk&_s_r_a=init"
        r=requests.get(url=url,timeout=10)
        r=r.text
        r=_handle_hk_hcg(r)
        df=pd.read_csv(StringIO(r),header=None,encoding='utf8')
        df.columns=TRD_COLShcg
        df['ticktime']=pd.to_datetime(df['ticktime'])
        df['symbol']=df['symbol'].map(lambda x: str(x).zfill(5))
        df=df.set_index('symbol')
    return df

def _handle_gqg(r):
    r=r.replace('changepercent','')
    r=r.replace('symbol','')
    r=r.replace('engname','') 
    r=r.replace('name','') 
    r=r.replace('tradetype','')
    r=r.replace('lasttrade','') 
    r=r.replace('prevclose','') 
    r=r.replace('high_52week','') 
    r=r.replace('low_52week','') 
    r=r.replace('open','') 
    r=r.replace('high','') 
    r=r.replace('low','') 
    r=r.replace('currentvolume','') 
    r=r.replace('volume','') 
    r=r.replace('amount','') 
    r=r.replace('ticktime','') 
    r=r.replace('buy','') 
    r=r.replace('sell','') 
    r=r.replace('eps','') 
    r=r.replace('dividend','') 
    r=r.replace('stocks_sum','') 
    r=r.replace('pricechange','') 
    r=r.replace('[{,','')
    r=r.replace('},','\n')
    r=r.replace('}]','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace(':','')
    r=r.replace(r'[','')
    return r




def get_hk_gqg_trading_sina():
    """
    获得国企股的交易数据
    -------------------
    Return
    """
    for i in xrange(1,2,1):
        url="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHKStockData?page=1&num=4000&sort=symbol&asc=1&node=gqg_hk&_s_r_a=init"
        r=requests.get(url=url,timeout=10)
        r=r.text
        r=_handle_gqg(r)
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=TRD_COLSgqg
        df['ticktime']=pd.to_datetime(df['ticktime'])
        df['symbol']=df['symbol'].map(lambda x: str(x).zfill(5))
        df=df.set_index('symbol')
    return df

def _handle_zz(r):
    r=r.replace("IO.XSRV2.CallbackList['dwC2mSZnEdWS48tY']([{",'')
    r=r.replace("IO.XSRV2.CallbackList['z6RpdMbIYp64ChXB']([{",'')
    r=r.replace('},','\n')
    r=r.replace('}])','')
    r=r.replace('"','')
    r=r.replace('{','')
    r=r.replace('}','')
    r=r.replace('symbol','')
    r=r.replace('name','')
    r=r.replace('trade','')
    r=r.replace('changes','')
    r=r.replace('close','')
    r=r.replace('open','')
    r=r.replace('high','')
    r=r.replace('low','')
    r=r.replace('volume','')
    r=r.replace('amount','')
    r=r.replace('day','')
    r=r.replace('aov','')
    r=r.replace('turnover','')
    r=r.replace(':','')
    r=r.replace('tag','')
    return r

def get_week_zd_sina():
    """
    获得周资金的情况
    ------
    Return
    """
    for i in xrange(1,2,1):
        #print i
        url="http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList%5B'dwC2mSZnEdWS48tY'%5D/StatisticsService.getSummaryWeekList?page={0}&num=50000&sort=changes&asc=0&node=adr_hk".format(i)
        r=requests.get(url=url).text
        r=_handle_zz(r)
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=week_COLS
        df['code']=df['symbol'].apply(lambda x: x[2::])
        del df['tag']
        df=df.drop_duplicates(subset='code')
        df=df.set_index('code')
    return df

def get_month_zd_sina():
    """
    获得月资金的情况
    ------
    Return
    """
    for i in xrange(1,2,1):
        #print i
        url="http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList%5B'z6RpdMbIYp64ChXB'%5D/StatisticsService.getSummaryMonthList?page={0}&num=50000&sort=changes&asc=0&node=adr_hk".format(i)
        r=requests.get(url=url).text
        r=_handle_zz(r)
        df=pd.read_csv(StringIO(r),header=None)
        df.columns=week_COLS
        df['code']=df['symbol'].apply(lambda x: x[2::])
        del df['tag']
        df=df.set_index('code')
    return df

def get_balance_sheet_sina(code):
    """
    获得个股的资产负责表
    -------
    Return
    """
    ticker = code
    urlFmt ='http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/%s/ctrl/all.phtml'
    url =  urlFmt % ticker
    print url
    df = pd.read_csv(url)
    return df

def get_income_statement_sina(code):
    """
    获得个股的利润表
    -------
    Return
    """    
    ticker = code
    urlFmt = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_ProfitStatement/displaytype/4/stockid/%s/ctrl/all.phtml'
    url =  urlFmt % ticker
    #print url
    df = pd.read_csv(url)

    return df

def get_cashflow_statement_sina(code):
    """
    获得个股的现金流量表
    -------
    Return
    """    
    ticker = code
    urlFmt = 'http://money.finance.sina.com.cn/corp/go.php/vDOWN_CashFlow/displaytype/4/stockid/%s/ctrl/all.phtml'
    url =  urlFmt % ticker
    #print url
    df = pd.read_csv(url)

    return df
def _handle_web_fi(code,year):
    _write_console()
    url='http://money.finance.sina.com.cn/corp/go.php/vFD_FinancialGuideLine/stockid/%s/ctrl/%s/displaytype/4.phtml' %(code,year)
    request = Request(url)
    text = urlopen(request, timeout=10).read()
    text = text.replace('--', '')
    html = lxml.html.parse(StringIO(text))
    res = html.xpath("//table[@id=\"BalanceSheetNewTable0\"]/*/tr")
    if PY3:
        sarr = [etree.tostring(node).decode('utf-8') for node in res]
    else:
        sarr = [etree.tostring(node) for node in res]
    sarr = ''.join(sarr)
    sarr = '<table>%s</table>'%sarr
    df = pd.read_html(sarr)[0]
    df=df.drop(0)
    df=df.drop(0,axis=1)
    df=df.drop(2)
    df=df.drop(13)
    df=df.drop(34)
    df=df.drop(39)
    df=df.drop(49)
    df=df.drop(69)
    df=df.drop(75)
    df=df.T
    df.columns =Ind_COLS
    return df
    
def get_financial_index_sina(code,current_year=datetime.datetime.today().year):
    """
    获得个股的财务指标
    ---------
    Return
    """
    _write_head()
    dataArr=pd.DataFrame()
    try:
        for year in xrange(current_year,1990,-1):
            try:
                df=_handle_web_fi(code,year)
                dataArr=dataArr.append(df,ignore_index=True)
            except:
                pass
        dataArr=dataArr.dropna(axis=0, how='all')
        dataArr=dataArr.drop_duplicates(subset='Date')
        dataArr['Date']=dataArr['Date'].astype(str)
        for label in DA_COLS:
            dataArr[label]=dataArr[label].astype(float)
        dataArr.sort_values(by='Date',inplace=True,ascending=True)
        try:
            del dataArr['Unnamed: 0']
        except:
            pass
        dataArr=dataArr.reset_index(drop=True)
        dataArr['EPS_Q']=dataArr['EPS_D']-dataArr['EPS_D'].shift(1)
        dataArr_l=dataArr.shape[0]
        for i in xrange(0,dataArr_l,1):
            if "03-31" in dataArr.ix[i,'Date']:
                dataArr.ix[i,'EPS_Q']=dataArr.ix[i,'EPS_D']
                #print dataArr.ix[i,'Date'],dataArr.ix[i,'EPS_D'],dataArr.ix[i,'EPS_Q']
        dataArr=dataArr.set_index('Date')
        return dataArr
    except Exception as e:
        print '\n',e
        return
#uro

def sina_index_handle(r):
    r=r.replace('var hq_str_b_','')
    r=r.replace('=',',')
    r=r.replace('"','')
    r=r.replace(';','')
    df=pd.read_csv(StringIO(r),header=None)
    df.columns=['code','name','close','change','chn_p','time']
    df['date']=today
    df=df.set_index('code')
    return df
#"""
def get_euro_sina_index():
    """
    获得欧洲指数数据
    -------------------------
    Return
    """
    urls=['http://hq.sinajs.cn/rn=6gbk6&list=b_ICEXI15,b_IT30,b_LUXXX,b_MDAX,b_NMX,b_NMDP,b_NSEL30,b_NTX,b_OBXP,b_NC70,b_N150,b_MS190,b_MED1,b_MSER,b_MSPE,b_N100,b_HEXT','http://hq.sinajs.cn/rn=5vo3x&list=b_SX5E,b_UKX,b_CAC,b_DAX,b_MICEX10,b_CN20,b_CM100,b_CS90,b_CRO,b_CLXP,b_CRTX,b_CH30,b_BUX,b_BVLX,b_CDAX,b_BIRS,b_CHTX,b_E300,b_FTSEM,b_FTSEMIB,b_FTSES,b_HDAX,b_HEX25,b_FTEFC1,b_FTEF80,b_ES30,b_BGCC200,b_EUE15P,b_EUETMP,b_FTASE,b_E100,b_BENMAX50,b_T1X,b_TALSE,b_SXXP,b_SXXE,b_SX5P,b_TDXP,b_TR20I,b_XU030,b_XU100,b_WBI,b_VLAM21,b_VILSE,b_AEX,b_AMX,b_AXX,b_BE500,b_ATX,b_PAX,b_HEXP,b_BELSTK,b_BELEXLIN,b_ASX,b_ASE,b_ATXPRIME,b_BEL20,b_BELEX15,b_BET,b_HEX,b_SAX,b_SASX10,b_SBF250,b_SBITOP,b_SE30,b_SBX,b_RIGSE,b_PXAP,b_OSEBX,b_OSEAX,b_OSEFX,b_OSESX,b_PSI20,b_SKSM,b_SLI,b_MCX,b_SVSM,b_MALTEX,b_MADX,b_MIDP,b_SPI,b_SPIEXX,b_SMI,b_SMIM,b_SMX,b_SPEURO,b_SPEU,b_OMX,b_OBX,b_ITLMS,b_ITMC,b_ITSTAR,b_KAX,b_LUXXR,b_KFX,b_INDEXCF,b_ISEQ,b_IBEX,b_PFTS,b_ICEXI']
    DataArr=pd.DataFrame()
    for url in urls:
        r=requests.get(url=url).text
        df=sina_index_handle(r)
        DataArr=DataArr.append(df)
    return DataArr
#asia
def get_asia_sina_index():
    """
    获得亚洲指数数据
    -------------------------
    Return
    """    
    url='http://hq.sinajs.cn/rn=someb&list=b_HSCI,b_NKY,b_KOSPI,b_TWSE,b_FSSTI,b_NKYJQ,b_SECTMIND,b_NKY500,b_SASEIDX,b_PCOMP,b_NEY,b_KSE,b_KSE30,b_KSE100,b_KWSEIDX,b_LQ45,b_SENSEX,b_MSM30,b_NIFTY,b_SET,b_TSEREIT,b_TSEMOTHR,b_TSE2,b_TW50,b_TWOTCI,b_VNINDEX,b_VHINDEX,b_TPX,b_TPXSM,b_TPX100,b_KRX100,b_TPX500,b_TPXC30,b_TPXM400,b_TPXL70,b_SET50,b_KOSPI50,b_FBMEMAS,b_DSM,b_DHAKA,b_FSTAS,b_HKSPGEM,b_HSCCI,b_HKSPLC25,b_DFMGI,b_CSEALL,b_BHSEEI,b_BHSEASI,b_BLOM,b_BSE100,b_BSE500,b_BSE200,b_HSCEI,b_HSF50,b_KLCI,b_JSDA,b_JOSMGNFF,b_KOSDAQ,b_KOSPI100,b_ADSMI,b_KOSPI2,b_JHERINX,b_JCI,b_HSFHK25,b_HSFCI,b_HSFML25,b_HSHFCI,b_HSMFCI,b_HSI,b_KOSTAR'
    r=requests.get(url=url).text
    df=sina_index_handle(r)
    return df
#america
def get_america_sina_index():
    """
    获得美洲指数数据
    -------------------------
    Return
    """    
    url='http://hq.sinajs.cn/rn=l7679&list=b_INDU,b_CCMP,b_SPX,b_SPTSX,b_IBOV,b_RAY,b_QIV,b_OEX,b_OSX,b_QMI,b_NYYID,b_NYP,b_NYA,b_NDX,b_NDF,b_NYE,b_NYID,b_NYLID,b_NYK,b_NYIID,b_RIY,b_SOX,b_XAX,b_XAU,b_UTY,b_XCI,b_XII,b_XOI,b_XMI,b_UTIL,b_TXEQ,b_NBI,b_SML,b_SPR,b_SPTSX60,b_TRAN,b_SPTSXVEN,b_RTY,b_MERVAL,b_DWCF,b_CUTL,b_CTRN,b_IBG,b_IBOVIEE,b_IBX50,b_IBVC,b_CRSMBCT,b_COMP,b_BURCAP,b_BSX,b_BKX,b_CBNK,b_CFIN,b_CINS,b_CIND,b_IBX,b_IGBC,b_JMSMX,b_IXK,b_IVBX2,b_KVY,b_MAR,b_MEXBOL,b_BBREIT,b_ITEL,b_ISP15,b_IIX,b_IGCX,b_IGBVL,b_IMC30,b_INMEX,b_ISBVL,b_IRT,b_MID'
    r=requests.get(url=url).text
    df=sina_index_handle(r)
    return df

#africa
def get_africa_sina_index():
    """
    获得非洲指数数据
    -------------------------
    Return
    """    
    url='http://hq.sinajs.cn/rn=8xf4l&list=b_TOP40,b_CASE,b_NSEIO,b_NGSEINDX,b_SEMDEX,b_TUSIBVMT,b_TUSISE,b_MOSENEW,b_MOSEMDX,b_INDI25,b_HERMES,b_JALSH,b_KNSMIDX,b_MCSINDEX,b_BGSMDC'
    r=requests.get(url=url).text
    df=sina_index_handle(r)
    return df
#ocea
def get_ocean_sina_index():
    """
    获得太平洋指数数据
    -------------------------
    Return
    """    
    url='http://hq.sinajs.cn/rn=3mrhx&list=b_AS30,b_NZSE50FG,b_NZSE,b_AS51,b_AS52,b_NZSE10'
    r=requests.get(url=url).text
    df=sina_index_handle(r)
    return df

def get_realtime_fc_sina(code):
    """
    获得商品期货的实时交易数据
    Parameters:
    -----------------
    code:String
      RB0 螺纹钢
      AG0 白银
      AU0 黄金
      CU0 沪铜
      AL0 沪铝
      ZN0 沪锌
      PB0 沪铅
      RU0 橡胶
      FU0 燃油
      WR0 线材
      A0 大豆
      M0 豆粕
      Y0 豆油
      J0 焦炭
      C0 玉米
      L0 乙烯
      P0 棕油
      V0 PVC
      RS0 菜籽
      RM0 菜粕
      FG0 玻璃
      CF0 棉花
      WS0 强麦
      ER0 籼稻
      ME0 甲醇
      RO0 菜油
      TA0 甲酸
      种名 + 0 （数字0），代表品种连续，如果是其他月份，请使用品种名 + YYYMM
    ktype：
        5、15、30、60分钟线
      --------------
    Return
    """
    code=code.upper()
    url='http://hq.sinajs.cn/list=%s' %code
    r=requests.get(url,timeout=10)
    r=r.content
    r=r.split('hq_str_',1)[1]
    r=r.replace('="',',')
    r=r.replace('";','')
    r=r.decode('gbk')
    df=pd.read_csv(StringIO(r),header=None)
    for i in [2,16,17,19,20,21,22,23,24,25,26,27,28]:
        df=df.drop(i,axis=1)
    df.columns=['code','name','open','high','low','pre-close','b1','s1','close','settle','pre-settle','bv1','sv1','hold','deal','date']
    return df

def _fcif_handle(r):
    r=r.content
    r=r.replace('],','\n')
    r=r.replace('[[','')
    r=r.replace(']]','')
    r=r.replace('"','')
    r=r.replace('[','')
    df=pd.read_csv(StringIO(r),header=None)
    df.columns=['date','open','high','low','close','volumn']
    return df

def get_hmin_fc(ktype,code):
    """
    Parameters:
    -----------------
    code:String
      RB0 螺纹钢
      AG0 白银
      AU0 黄金
      CU0 沪铜
      AL0 沪铝
      ZN0 沪锌
      PB0 沪铅
      RU0 橡胶
      FU0 燃油
      WR0 线材
      A0 大豆
      M0 豆粕
      Y0 豆油
      J0 焦炭
      C0 玉米
      L0 乙烯
      P0 棕油
      V0 PVC
      RS0 菜籽
      RM0 菜粕
      FG0 玻璃
      CF0 棉花
      WS0 强麦
      ER0 籼稻
      ME0 甲醇
      RO0 菜油
      TA0 甲酸
      种名 + 0 （数字0），代表品种连续，如果是其他月份，请使用品种名 + YYYMM
    ktype：
        5、15、30、60分钟线
      --------------
    Return
    """
    code=code.upper()
    url='http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesMiniKLine%sm?symbol=%s' %(ktype,code)
    r=requests.get(url,timeout=10)
    df=_fcif_handle(r)
    return df

def get_hmin_if(ktype,code):
    """
    Parameters:
    -----------------
      IF 股指期货
      请使用品种名 + YYMM
      --------------
    Return
    """
    url='http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesMiniKLine%sm?symbol=%s' %(ktype,code)
    r=requests.get(url,timeout=10)
    df=_fcif_handle(r)
    return df

def get_hday_fc(code):
    """
    Parameters:
    -----------------
    code:String
      RB0 螺纹钢
      AG0 白银
      AU0 黄金
      CU0 沪铜
      AL0 沪铝
      ZN0 沪锌
      PB0 沪铅
      RU0 橡胶
      FU0 燃油
      WR0 线材
      A0 大豆
      M0 豆粕
      Y0 豆油
      J0 焦炭
      C0 玉米
      L0 乙烯
      P0 棕油
      V0 PVC
      RS0 菜籽
      RM0 菜粕
      FG0 玻璃
      CF0 棉花
      WS0 强麦
      ER0 籼稻
      ME0 甲醇
      RO0 菜油
      TA0 甲酸
      种名 + 0 （数字0），代表品种连续，如果是其他月份，请使用品种名 + YYMM
      --------------
    Return
    """
    code=code.upper()
    url='http://stock2.finance.sina.com.cn/futures/api/json.php/IndexService.getInnerFuturesDailyKLine?symbol=%s' %(code)
    r=requests.get(url,timeout=10)
    df=_fcif_handle(r)
    return df

def get_hday_if(code):
    code=code.upper()
    url='http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesDailyKLine?symbol=%s' %(code)
    r=requests.get(url,timeout=10)
    df=_fcif_handle(r)
    return df

def get_ddV(code,unit,date=datetime.datetime.today()):
    """
    获得按成交量统计的大单数据
    --------------
    unit is the deal unit, the volume is unit 100 times
    --------------
    Return:
    """
    volume=int(unit)*100
    if code[0]=='6' or code[0]=='9':
        code='sh'+code
    else:
        code='sz'+code
    url='http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_download.php?symbol=%s&num=600000&page=1&sort=ticktime&asc=0&volume=%s&amount=0&type=0&day=%s'%(code,volume,date)
    try:
        df=pd.read_csv(url,header=None)#,encoding='gb18030')
        df=df.drop(0)
        df.columns=['code','name','time','price','volume','pre-price','type']
        df.name=df['name'].map(lambda x:str(x).decode('gbk'))
        df['date']=date
        df['type']=df['type'].map(lambda x:str(x).decode('gbk'))
        for label in ['price','volume','pre-price']:
            df[label]=df[label].astype(float)  
        print df.groupby('type').sum()      
        return df
    except Exception as e:
        print (e)

        return

def get_ddA(code,amount,date=datetime.datetime.today()):
    """
    获得以成交量统计的大单数据
    ------------------
    the Amount is unit 0000,so the amount will be 10000,
    times for the input data
    -------------------
    Return
    """
    amount=int(amount)*10000
    if code[0]=='6' or code[0]=='9':
        code='sh'+code
    else:
        code='sz'+code
    url='http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_download.php?symbol=%s&num=600000&page=1&sort=ticktime&asc=0&volume=0&amount=%s&type=0&day=%s'%(code,amount,date)
    try:
        df=pd.read_csv(url,header=None)#,encoding='gb18030')
        df=df.drop(0)
        df.columns=['code','name','time','price','volume','pre-price','type']
        df.name=df['name'].map(lambda x:str(x).decode('gbk'))
        df['date']=date
        df['type']=df['type'].map(lambda x:str(x).decode('gbk'))
        for label in ['price','volume','pre-price']:
            df[label]=df[label].astype(float)
        print df.groupby('type').sum()      
        return df
    except Exception as e:
        print (e)

def get_ddT(code,amount,date=datetime.datetime.today()):
    """
    获得以大单倍数的成交数据
    1 stand for 5(x),2 for 10(X),3 for 20(X),4 for 50(X),5 for 100(X)
    """
    if code[0]=='6' or code[0]=='9':
        code='sh'+code
    else:
        code='sz'+code
    url='http://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill_download.php?symbol=%s&num=600000&page=1&sort=ticktime&asc=0&volume=0&amount=0&type=%s&day=%s'%(code,amount,date)
    try:
        df=pd.read_csv(url,header=None)#,encoding='gb18030')
        df=df.drop(0)
        df.columns=['code','name','time','price','volume','pre-price','type']
        df.name=df['name'].map(lambda x:str(x).decode('gbk'))
        df['date']=date
        df['type']=df['type'].map(lambda x:str(x).decode('gbk'))
        for label in ['price','volume','pre-price']:
            df[label]=df[label].astype(float)
        print df.groupby('type').sum()
        return df
    except Exception as e:
        print (e)
#df=get_euro_index()
def get_predict(mytype):
    """
        获取机构对上市公司净利润的预测数据
    Parameters
    --------
      mytype:
           roe,净资产收益率%
           sales,营业收入，亿元
           eps,每股收益，元
           np,净利润，亿元
    Return
    --------
    DataFrame
        code,代码
        name,名称
        roe,净资产收益率(%)
        report_date,发布日期
        institute,研究机构
        staff,研究员
        astra,摘要
    """
    _write_head()
    df =  _get_predict_data(mytype,1, pd.DataFrame())
    if df is not None:
        #             df = df.drop_duplicates('code')
        #df['code'] = df['code'].map(lambda x:str(x).zfill(6))
        pass
    return df


def _get_predict(mytype,pageNo, dataArr):
    _write_console()
    url='http://vip.stock.finance.sina.com.cn/q/go.php/vPerformancePrediction/kind/%s/index.phtml?num=60&p=%s'%(mytype,pageNo)
    try:
        request = Request(url)
        print url
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        #df = df.drop(11, axis=1)
        df.columns = ['code','name','last','current','next_1','next_2','report_date','institute','staff','abstr']
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        #return dataArr
        #"""
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_predict_data(mytype,pageNo,dataArr)
        else:
            return dataArr
        #"""
    except Exception as e:
        print(e)

def get_predict_percode(mytype,code):
    """
        获取机构对上市公司净利润的预测数据
    Parameters
    --------
       mytype:
           roe,净资产收益率%
           sales,营业收入，亿元
           eps,每股收益，元
           np,净利润，亿元
      code:上海或深圳交易所的股份代码，6个数字字符
    Return
    --------
    DataFrame
        code,代码
        name,名称
        roe,净资产收益率(%)
        report_date,发布日期
        institute,研究机构
        staff,研究员
        astra,摘要
    """
    _write_head()
    df =  _get_predict_data_percode(mytype,code,1, pd.DataFrame())
    if df is not None:
        #             df = df.drop_duplicates('code')
        #df['code'] = df['code'].map(lambda x:str(x).zfill(6))
        pass
    return df


def _get_predict_data_percode(mytype,code,pageNo, dataArr):
    _write_console()
    url='http://vip.stock.finance.sina.com.cn/q/go.php/vPerformancePrediction/kind/%s/index.phtml?symbol=%s&num=60&p=%s'%(mytype,code,pageNo)
    try:
        request = Request(url)
        print url
        text = urlopen(request, timeout=10).read()
        text = text.decode('GBK')
        text = text.replace('--', '')
        html = lxml.html.parse(StringIO(text))
        res = html.xpath("//table[@class=\"list_table\"]/tr")
        if PY3:
            sarr = [etree.tostring(node).decode('utf-8') for node in res]
        else:
            sarr = [etree.tostring(node) for node in res]
        sarr = ''.join(sarr)
        sarr = '<table>%s</table>'%sarr
        df = pd.read_html(sarr)[0]
        #df = df.drop(11, axis=1)
        df.columns = ['code','name','last','current','next_1','next_2','report_date','institute','staff','abstr']
        dataArr = dataArr.append(df, ignore_index=True)
        nextPage = html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')
        #return dataArr
        #"""
        if len(nextPage)>0:
            pageNo = re.findall(r'\d+', nextPage[0])[0]
            return _get_predict_data_percode(mytype,code,pageNo, dataArr)
        else:
            return dataArr
        #"""
    except Exception as e:
        print(e)
