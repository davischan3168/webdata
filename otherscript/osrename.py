# encoding:utf-8
##
# 文件名如:
# 贺龙传奇\d+[有声下吧www.ysx8.com].mp3
##
import os,re
import sys
pf=sys.argv[1]
print (pf)
fs=os.listdir(pf)
for f in fs:
    #newone=f.replace('G','ggggg')
    newone=f+'.pdf'
    os.rename(pf+f,pf+newone)
    print (f,newone)
