# --*- coding:utf-8 -*--
"""
收集在电脑中的文件
文件所在的目录为path
收集的文件名输出在bk的文件中
"""
import os,sys

path=sys.argv[1]

def f_write(path,content):
    f=open(path,'a')
    f.write(content)
    f.flush

def collect_book_iso(path):
    """
    将path的iso文件挂载到/mnt/iso目录中
    然后将iso里的文件全部输出到bk的文件中
    """
    cmd_mount='sudo mount -t iso9660 -o loop %s /mnt/iso' %path
    os.system(cmd_mount)
    for r,dirsname,ffiles in os.walk('/mnt/iso'):
        line='-d %s \n' %r
        f_write(bk,line)
        for fl in ffiles:
            path=os.path.join(r,fl)
            line='-f %s \n'%path
            f_write(bk,line)
    os.system('sudo umount /mnt/iso')
    return


def book_collect(path):
    """
    将path目录中的文件输出到bk
    文件中。
    """
    for root,dirs,files in os.walk(path):
        line='-d %s\n'%root
        f_write(bk,line)
        for f in files:
            fn=os.path.splitext(f)
            if fn[1]=='.iso':
                fullpath=os.path.join(root,f)
                collect_book_iso(fullpath)
            elif fn[1] in ['.rar','zip']:
                fullpath1=os.path.join(root,f)
                line='-f %s \n'%fullpath1
                f_write(bk,line)
            else:
                fullpath1=os.path.join(root,f)
                line='-f %s \n'%fullpath1
                f_write(bk,line)                
    return
                

bk=sys.argv[2]
book_collect(path)

