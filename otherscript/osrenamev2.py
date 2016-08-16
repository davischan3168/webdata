# encoding:utf-8
##
# 实现批量修改文件夹下说有文件的名称，循环所有的文件夹
# 
##
import os,re
import sys
pf=sys.argv[1]
print (pf)
#fs=os.listdir(pf)
for (pf,dirs,files) in os.walk(pf):
    for old in files:
        #print filename
        #"""
        tem=old.replace('[','(')
        new=tem.replace(']',')')
        os.rename(pf+'/'+old,pf+'/'+new)
        print (old,new)
        #"""
