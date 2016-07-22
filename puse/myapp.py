import pandas as pd
import numpy as np
try:
    import tushare as ts
except Exception as e:
    print e
import os,sys
try:
    import Quandl
except:
    import quandl as Quandl
import datetime,time
import webdata.puse.sina as sn
import webdata.puse.eastmoney as em
import webdata.puse.aastock as ast
import webdata.puse.jqka as ths
token="ALM9oCUNixBCkHwyxJHF"
today = time.strftime("%Y-%m-%d")
start_time="2001-01-01"
end_time=today
bftoday=str(datetime.date.today()-datetime.timedelta(days=1))

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
        print 'Getting Data for %s'% ticker
        try:
            df= Quandl.get(ticker, authtoken=token, trim_start=start_time,trim_end=end_time)
            df.to_csv(fn)
            print df.tail()
            return df
        except Exception as e:
            print e#"Getting data is error"
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
            print 'Updating Data from %s for %s.'% (bday,ticker)
            try:
                df1= Quandl.get(ticker, authtoken=token, trim_start=bday,trim_end=end_time)
                df= all_data1.append(df1)
                if df.empty==False:
                    print df1.tail()
                    df.to_csv(fn, header=None, mode='a')
                return df
            except Exception as e:
                print e#"Getting data is error"
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
            print 'Updating Data from %s for %s.'% (bday,ticker)
            try:
                df1= Quandl.get(ticker, authtoken=token, trim_start=bday,trim_end=end_time)
                df2= all_data1.append(df1)
                if df2.empty==False:
                    df=dff.append(df2)
                    print df1.tail()
                    h5[ticker]=df
                h5.close()
                return df
            except Exception as e:
                print e#"Getting data is error"
                return
    except Exception as e:
        print 'Getting Data for %s'% ticker
        try:
            df= Quandl.get(ticker, authtoken=token, trim_start=start_time,trim_end=end_time)
            h5[ticker]=df
            print df.tail()
            h5.close()
            return df
        except Exception as e:
            print e#"Getting data is error"
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
            print '\nUpdating data from %s for %s:'%(tem,code)
            t=time.strptime(tem,"%Y-%m-%d")
            y,m,d = t[0:3]
            tt=datetime.datetime(y,m,d)
            bd=tt+datetime.timedelta(days=1)
            #if bd.weekday()==5:
            #    bd = bd+datetime.timedelta(days=2)
            #    print 'It is Sat'
            bday=bd.strftime('%Y-%m-%d')
            all_data1 = pd.DataFrame()
            all_data = ts.get_h_data(code,autype=None,start=bday, end=today)
            all_data1 = all_data1.append(all_data)
            if all_data1.empty==False:
                print all_data1.head(1)
                all_data1.sort_index(ascending=True,inplace=True)
                df=ddf.append(all_data1)
                h5[code]=df
                return df
    except Exception as e:
        print e
        print '\nDownloading the data %s:'%code
        df= ts.get_h_data(code,autype=None,start='2000-01-01', end=today)
        df.sort_index(ascending=True,inplace=True)
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
            print '\nUpdating data from %s for %s:'%(tem,code)
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
                all_data = ts.get_hist_data(code,start=bday, end=today)
                #print all_data
                all_data1 = all_data1.append(all_data)
                if all_data1.empty==False:
                    all_data1.sort_index(ascending=True,inplace=True)
                    df=dff.append(all_data1)
                    #print df
                    h5[code]=df
                    return df
            except Exception as e:
                print e,'No data for %s to upadate'%code
                return 
    except Exception as e:
        print e
        print 'Getting the data for %s: \n'%code
        df=ts.get_hist_data(code)
        df.sort_index(ascending=True,inplace=True)
        h5[code]=df
        #h5.close()
        return df

#get_myquandl("DY4/000001")
#df=get_myquandl("LLOYDS/BPI")
#df=get_data_last3year('600422')
