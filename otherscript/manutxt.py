## encoding:utf-8
import os,sys,re
import string

pf=sys.argv[1]

my_f=open(pf,'r')
lines=my_f.readlines()
my_f.close()
pfp=os.path.splitext(pf)[0]+'_1amend.txt'

def _save_file(pfp,content):
    savef=open(pfp,'a')
    savef.write(content)
    savef.write('\n')
    savef.flush()

for line in lines:
    line=line.strip()
    if line!='·全唐诗·' and line !='':
        print(line)
        _save_file(pfp,line)
