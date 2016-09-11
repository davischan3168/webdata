# encoding:utf-8
##
# 实现批量修改文件夹下说有文件的名称，循环所有的文件夹
# 
##
import os,re
import sys
pf=sys.argv[1]
#print (pf)
#fs=os.listdir(pf)
def write_file(path,r):
    f=open(path,'a')
    f.write(r)
    f.flush()
    #f.close()
    #return

titles='''
#+TITLE: Change to Name
#+AUTHOR: Davis Chen
#+DATE: today
#+EMAIL: chenzuliang@163.com
#+DESCRIPTION: the page description, e.g. for the XHTML meta tag
#+KEYWORDS: the page keywords, e.g. for the XHTML meta tag
#+LANGUAGE: language for HTML, e.g. ‘en’ (org-export-default-language)
#+TEXT: Some descriptive text to be inserted at the beginning.
#+STYLE: <link rel="stylesheet" type="text/css" href="./worg.css" />
#+TEXT: Several lines may be given.
#+OPTIONS: H:5 num:t toc:t \\n:nil @:t ::t |:t ^:t f:t TeX:t ...
#+LINK_UP: the ``up'' link of an exported page
#+LINK_HOME: the ``home'' link of an exported page
#+TODO: TODO(t!/@) INPROGRESS(n!/@) WAITING(w!/@)| DONE(d!/@) CANCEL(c!/@)
#+TAGS: @office(o) @home(h) @traffic(t)
#+TAGS: computer(c) nocomputer(n) either(e)
#+TAGS: immediately(i) wait(w) action(a)
'''
pfname=pf.replace('/','')
with open(pfname+'_connent.org','w') as f:
    f.writelines(titles)
    f.flush()

def delet_file(pf):
    for (pf,dirs,files) in os.walk(pf):
        for old in files:
            if '_content.txt' in os.path.split(old)[1]:
                rmfile=os.path.join(pf,old)
                os.remove(rmfile)

#delet_file(pf)

for (pf,dirs,files) in os.walk(pf):
    for old in files:
        if (os.path.splitext(old)[1]!='tmp') and \
        (re.match(r'^~\$',os.path.splitext(old)[0]) is None):
            #过滤临时文件
            filename=os.path.splitext(old)[0]
            line= '- [ ]  [[./'+pf+'/'+old+']['+filename+']]\n'
            write_file('wa.org',line)
