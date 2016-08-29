y# -*- encoding:utf-8 -*-
##
# 实现批量修改文件夹下说有文件的名称，循环所有的文件夹
# 
##
import os,re
import sys
pf=sys.argv[1]
print (pf)
#fs=os.listdir(pf)
def write_file(path,r):
    f=open(path,'a')
    f.write(r)
    f.close()
    return

for (pf,dirs,files) in os.walk(pf):
    for old in files:
        try:
            #new=tem.replace(']',')')
            #os.rename(pf+'/'+old,pf+'/'+new)
            filename=os.path.splitext(old)[0]
            line= '- [ ]  [[./'+pf+'/'+old+']['+filename+']]\n'
            write_file('wa.txt',line)
            #print (old,new)
            #"""
        except Exception as e:
            print (e)
