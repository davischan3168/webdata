# -*- coding:utf-8 -*- 
import pandas as pd
import numpy as np
import webdata.stock.trading as wt
import webdata.stock.fundamental as wf
import os,sys
try:
    import Quandl
except:
    import quandl as Quandl
import datetime,time
token="ALM9oCUNixBCkHwyxJHF"
today = time.strftime("%Y-%m-%d")
start_time="2001-01-01"
end_time=today
bftoday=str(datetime.date.today()-datetime.timedelta(days=1))
import tushare as ts
def annlysis_shares_holdbyfund(code):
    pf='./stockdata/data/share_hold_by_fund.csv'
    df=pd.read_csv(pf,encoding='gbk',low_memory=False,index_col=0)
    df.code=df.code.map(lambda x:str(x).zfill(6))
    dff=df[df.code==code]
    dfff=dff.groupby('date')
    dffff=dfff.sum()
    return dffff

def get_myquandl(ticker):
    fn='./Quandl/'+ticker+'.csv'
    if not os.path.exists(fn):
        pf=os.path.split(fn)[0]
        #print pf
        if not os.path.exists(pf):
            os.mkdir(pf)
        print ('Getting Data for %s'% ticker)
        try:
            df= Quandl.get(ticker, authtoken=token, trim_start=start_time,trim_end=end_time)
            df.to_csv(fn)
            print (df.tail())
            return df
        except Exception as e:
            print (e)#"Getting data is error"
            #pass
            return
    else:
        all_data=pd.read_csv(fn)
        tem=all_data.iloc[-1]['Date']
        if tem != bftoday:
            t=time.strptime(tem,"%Y-%m-%d")
            y,m,d = t[0:3]
            tt=datetime.datetime(y,m,d)
            bd=tt+datetime.timedelta(days=1)
            bday=bd.strftime('%Y-%m-%d')
            all_data1 = pd.DataFrame()
            print ('Updating Data from %s for %s.'% (bday,ticker))
            try:
                df1= Quandl.get(ticker, authtoken=token, trim_start=bday,trim_end=end_time)
                df= all_data1.append(df1)
                if df.empty==False:
                    print (df1.tail())
                    df.to_csv(fn, header=None, mode='a')
                return df
            except Exception as e:
                print (e)#"Getting data is error"
                return

def get_myquandl_hdf5(ticker):
    h5path='./testh5df/Quandl.h5'
    if os.path.exists(h5path):
        h5 = pd.HDFStore(h5path,'a', complevel=4,complib='blosc')
    else:
        h5 = pd.HDFStore(h5path,'w', complevel=4,complib='blosc')
    try:
        dff=h5[ticker]
        tem=str(dff.index[-1])[0:10]
        if tem != bftoday:
            t=time.strptime(tem,"%Y-%m-%d")
            y,m,d = t[0:3]
            tt=datetime.datetime(y,m,d)
            bd=tt+datetime.timedelta(days=1)
            bday=bd.strftime('%Y-%m-%d')
            all_data1 = pd.DataFrame()
            print ('Updating Data from %s for %s.'% (bday,ticker))
            try:
                df1= Quandl.get(ticker, authtoken=token, trim_start=bday,trim_end=end_time)
                df2= all_data1.append(df1)
                if df2.empty==False:
                    df=dff.append(df2)
                    #print df1.tail()
                    h5[ticker]=df
                h5.close()
                return df
            except Exception as e:
                print (e)#"Getting data is error"
                return
    except Exception as e:
        print ('Getting Data for %s'% ticker)
        try:
            df= Quandl.get(ticker, authtoken=token, trim_start=start_time,trim_end=end_time)
            h5[ticker]=df
            print (df.tail())
            h5.close()
            return df
        except Exception as e:
            print (e)#"Getting data is error"
            return
            
def get_history_data_mp(code):
    h5path='./testh5df/stockdata_history.h5'
    if os.path.exists(h5path):
        h5 = pd.HDFStore(h5path,'a', complevel=4,complib='blosc')
    else:
        h5 = pd.HDFStore(h5path,'w', complevel=4,complib='blosc')
    try:
        ddf=h5[code]
        #dftem=datetime.datetime.strftime('%Y-%m-%d',ddf.index[-1])
        dftem=str(ddf.index[-1])[0:10]
        tem=dftem
        if tem != bftoday:
            print ('\nUpdating data from %s for %s:'%(tem,code))
            t=time.strptime(tem,"%Y-%m-%d")
            y,m,d = t[0:3]
            tt=datetime.datetime(y,m,d)
            bd=tt+datetime.timedelta(days=1)
            #if bd.weekday()==5:
            #    bd = bd+datetime.timedelta(days=2)
            #    print 'It is Sat'
            bday=bd.strftime('%Y-%m-%d')
            all_data1 = pd.DataFrame()
            all_data = wt.get_h_data(code,autype=None,start=bday, end=today)
            all_data1 = all_data1.append(all_data)
            if all_data1.empty==False:
                #print all_data1.head(1)
                #all_data1.sort_index(ascending=True,inplace=True)
                df=ddf.append(all_data1)
                h5[code]=df
                return df
    except Exception as e:
        print (e)
        print ('\nDownloading the data %s:'%code)
        df= wt.get_h_data(code,autype=None,start='2000-01-01', end=today)
        #df.sort_index(ascending=True,inplace=True)
        h5[code]=df
        #h5.close()
        return df

def get_data_last3year_mp(code):
    h5path='./testh5df/stockdata_last3year.h5'
    if os.path.exists(h5path):
        h5 = pd.HDFStore(h5path,'a', complevel=4,complib='blosc')
    else:
        h5 = pd.HDFStore(h5path,'w', complevel=4,complib='blosc')
    try:
        dff=h5[code]
        tem=str(dff.index[-1])[0:10]
        if tem < bftoday:
            print ('\nUpdating data from %s for %s:'%(tem,code))
            t=time.strptime(tem,"%Y-%m-%d")
            y,m,d = t[0:3]
            tt=datetime.datetime(y,m,d)
            bd=tt+datetime.timedelta(days=1)
            #if bd.weekday()==5:
            #    bd = bd+datetime.timedelta(days=2)
            #    print 'It is Sat'
            bday=bd.strftime('%Y-%m-%d')
            all_data1 = pd.DataFrame()
            try:
                all_data = wt.get_hist_data(code,start=bday, end=today)
                #print all_data
                all_data1 = all_data1.append(all_data)
                if all_data1.empty==False:
                    #all_data1.sort_index(ascending=True,inplace=True)
                    df=dff.append(all_data1)
                    #print df
                    h5[code]=df
                    return df
            except Exception as e:
                print (e,'No data for %s to upadate'%code)
                return 
    except Exception as e:
        print (e)
        print ('Getting the data for %s: \n'%code)
        df=wt.get_hist_data(code)
        #df.sort_index(ascending=True,inplace=True)
        h5[code]=df
        #h5.close()
        return df


def get_h_hdf5(code):
    """
    获取历史复权数据，分为前复权和后复权数据，接口提供股票上市以来所有历史数据，默认为前复权。如果不设定开始和结束日期，则返回近一年的复权数据，从性能上考虑，推荐设定开始日期和结束日期，而且最好不要超过三年以上，获取全部历史数据，请分年段分步获取，取到数据后，请及时在本地存储。
    """
    h5path='./testh5df/stockdata.h5'
    if os.path.exists(h5path):
        h5 = pd.HDFStore(h5path,'a', complevel=4,complib='blosc')
    else:
        h5 = pd.HDFStore(h5path,'w', complevel=4,complib='blosc')
    if code[0]=='0' or code[0]=='3' or code[0]=='2':
        label='M/sz'+code
    elif code[0]=='6' or code[0]=='9':
        label='M/ss'+code
    
    try:
        dd=h5[label]
        tem=str(dd.index[-1])[0:10]
        if tem!=today:
            if datetime.datetime.today().isoweekday() in [1,2,3,4,5]:
                #print 'Updating the data from%s for %s:'%(tem,code)
                t=time.strptime(tem,'%Y-%m-%d')
                y,m,d=t[0:3]
                tt=datetime.datetime(y,m,d)
                bd=tt+datetime.timedelta(days=1)
                bday=bd.strftime('%Y-%m-%d')
                df1=wt.get_h_data(code,start=bday,end=today)
                #df1=df1.sort_index(ascending=True,inplace=True)
                df=dd.append(df1)
                #df=df.sort_index(ascending=True)
                h5.append(label,df,data_columns=df.columns)
    except:
        df=wt.get_h_data(code)
        #df=df.sort_index(ascending=True)
        h5.append(label,df,data_columns=df.columns)
    #finally:
    #    h5.close()
    df.index=pd.to_datetime(df.index)
    return df

            


def get_hist_hdf5(code):
    """
    获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据
    """
    h5path='./testh5df/stockdata.h5'
    if os.path.exists(h5path):
        h5 = pd.HDFStore(h5path,'a', complevel=4,complib='blosc')
    else:
        h5 = pd.HDFStore(h5path,'w', complevel=4,complib='blosc')
    if code[0]=='0' or code[0]=='3' or code[0]=='2':
        label='l3y/sz'+code
    elif code[0]=='6' or code[0]=='9':
        label='l3y/ss'+code
    
    try:
        dd=h5[label]
        tem=str(dd.index[-1])[0:10]
        if tem!=today:
            if datetime.datetime.today().isoweekday() in [1,2,3,4,5]:
                #print 'Updating the data from%s for %s:'%(tem,code)
                t=time.strptime(tem,'%Y-%m-%d')
                y,m,d=t[0:3]
                tt=datetime.datetime(y,m,d)
                bd=tt+datetime.timedelta(days=1)
                bday=bd.strftime('%Y-%m-%d')
                df1=wt.get_hist_data(code,start=bday,end=today)
                df=dd.append(df1)
                #df=df.sort_index(ascending=True,inplace=True)
                h5.append(label,df,data_columns=df.columns)
    except:
        df=wt.get_hist_data(code)
        #df=df.sort_index(ascending=True,inplace=True)                
        h5.append(label,df,data_columns=df.columns)
    #finally:
    #    h5.close()
    df.index=pd.to_datetime(df.index)
    return df

def get_open_hist_hdf5(code,h5):
    """
    获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据
    """
    if code[0]=='0' or code[0]=='3' or code[0]=='2':
        label='l3y/sz'+code
    elif code[0]=='6' or code[0]=='9':
        label='l3y/ss'+code
    try:
        df=h5[label]
        #print(df)
        tem=str(df.index[-1])[0:10]
        if tem<today:
            if datetime.datetime.today().isoweekday() in [1,2,3,4,5]:
                t=time.strptime(tem,'%Y-%m-%d')
                y,m,d=t[0:3]
                tt=datetime.datetime(y,m,d)
                bd=tt+datetime.timedelta(days=1)
                bday=bd.strftime('%Y-%m-%d')
                df1=wt.get_hist_data(code,start=bday,end=today)
                #print(df1)
                df=df.append(df1)
                df.index=pd.to_datetime(df.index)
                #df=df.sort_index(ascending=True)
                #print(df)
                h5[label]=df
    except:
        df=wt.get_hist_data(code)
        #print (df)
        if df is not None:
            #df.index=pd.to_datetime(df.index)
            #df=df.sort_index(ascending=True)
            h5[label]=df
    finally:
        pass
    return df

def get_open_h_hdf5(code,h5):
    """
    获取个股全部历史交易数据
    """
    if code[0]=='0' or code[0]=='3' or code[0]=='2':
        label='M/sz'+code
    elif code[0]=='6' or code[0]=='9':
        label='M/ss'+code
    try:
        df=h5[label]
        tem=str(df.index[-1])[0:10]
        if tem<today:
            if datetime.datetime.today().isoweekday() in [1,2,3,4,5]:
                t=time.strptime(tem,'%Y-%m-%d')
                y,m,d=t[0:3]
                tt=datetime.datetime(y,m,d)
                bd=tt+datetime.timedelta(days=1)
                bday=bd.strftime('%Y-%m-%d')
                df1=wt.get_h_data(code,start=bday,end=today)
                df=df.append(df1)
                #df.index=pd.to_datetime(df.index)
                #df=df.sort_index(ascending=True)
                #print(df)
                h5[label]=df
    except:
        tem = wf.get_stock_basics()
        date=tem.ix[code]['timeToMarket']
        t=time.strptime(str(date),'%Y%m%d')
        startt=time.strftime('%Y-%m-%d',t)
        df=wt.get_h_data(code,start=startt,end=today)
        if df is not None:
            #df.index=pd.to_datetime(df.index)
            #df=df.sort_index(ascending=True)
            h5[label]=df
    finally:
        pass
    return df

def open_hdf5():
    h5path='./testh5df/stockdata.h5'
    if os.path.exists(h5path):
        h5 = pd.HDFStore(h5path,'a', complevel=4,complib='blosc')
    else:
        h5 = pd.HDFStore(h5path,'w', complevel=4,complib='blosc')
    return h5

def get_h_csv(code):
    """
    获取历史复权数据，分为前复权和后复权数据，接口提供股票上市以来所有历史数据，默认为前复权。如果不设定开始和结束日期，则返回近一年的复权数据，从性能上考虑，推荐设定开始日期和结束日期，而且最好不要超过三年以上，获取全部历史数据，请分年段分步获取，取到数据后，请及时在本地存储。
    """
    h5path='./stockdata/data/'+code+'.csv'
    if not os.path.exists(h5path):
        tem = wf.get_stock_basics()
        date=tem.ix[code]['timeToMarket']
        t=time.strptime(str(date),'%Y%m%d')
        startt=time.strftime('%Y-%m-%d',t)
        df=wt.get_h_data(code,start=startt,end=today)
        #df.index=pd.to_datetime(df.index)
        #df=df.sort_index(ascending=True)
        df.to_csv(h5path)
    else:
        df=pd.read_csv(h5path,index_col='date')
        tem=str(df.index[-1])[0:10]
        if tem<today:
            if datetime.datetime.today().isoweekday() in [1,2,3,4,5]:
                t=time.strptime(tem,'%Y-%m-%d')
                y,m,d=t[0:3]
                tt=datetime.datetime(y,m,d)
                bd=tt+datetime.timedelta(days=1)
                bday=bd.strftime('%Y-%m-%d')
                df1=wt.get_h_data(code,start=bday,end=today)
                if df1 is not None:
                    #df1.index=pd.to_datetime(df1.index)
                    #df1=df1.sort_index(ascending=True)                    
                    df=df.append(df1)
                    df1.to_csv(h5path,mode='a',header=None)
    return df

def get_hist_csv(code):
    
    """
    获取个股历史交易数据（包括均线数据），可以通过参数设置获取
    日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据
    """
    h5path='./stockdata/data/'+code+'.csv'
    if not os.path.exists(h5path):
        df=wt.get_hist_data(code)
        if df is not None:
            #df.index=pd.to_datetime(df.index)
            #df=df.sort_index(ascending=True)
            df.to_csv(h5path)
    else:
        df=pd.read_csv(h5path,index_col='date')
        tem=str(df.index[-1])[0:10]
        if tem!=today:
            if datetime.datetime.today().isoweekday() in [1,2,3,4,5]:
                t=time.strptime(tem,'%Y-%m-%d')
                y,m,d=t[0:3]
                tt=datetime.datetime(y,m,d)
                bd=tt+datetime.timedelta(days=1)
                bday=bd.strftime('%Y-%m-%d')
                df1=wt.get_hist_data(code,start=str(bday),end=str(today))
                if df1 is not None:
                    #df1.index=pd.to_datetime(df.index)
                    #df1=df1.sort_index(ascending=True)
                    df=df.append(df1)
                    df1.to_csv(h5path,mode='a',header=None)
    return df

#get_myquandl("DY4/000001")
#df=get_myquandl("LLOYDS/BPI")
#df=get_data_last3year('600422')
