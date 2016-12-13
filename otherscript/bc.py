# --*- coding:utf-8 -*--
"""
收集在电脑中的文件
文件所在的目录为path
收集的文件名输出在bk的文件中
"""
import os,sys

booktype=['.txt','.pdf','.mobi','.epub','.pdg','.doc','.docx','.htm','.chm','.exe','.ppt','.azw3']

archive=['.zip','.rar']

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
            """
            if os.path.splitext(fl)[1].lower() in booktype:
                path=os.path.join(r,fl) e
                line='-f %s \n'%path
                f_write(bk,line)
            elif os.path.splitext(fl)[1].lower() in archive:
                pathf=os.path.join(r,fl)
                comressfile_listname(pathf,bk)
            """
    os.system('sudo umount /mnt/iso')
    return

def comressfile_listname(compressfile,bk):
    #print(compressfile)
    ftype=os.path.splitext(compressfile)[1]
    if ftype in ['.zip']:
        print('It is zipfile')
        os.system('unzip -l %s > temp.txt'%compressfile)
        try:
            read_filezip('temp.txt',bk)
        except Exception as e:
            print(compressfile,e)
    elif ftype in ['.rar']:
        print('It is rarfile')
        os.system('unrar l %s > temp.txt'%compressfile)
        try:
            read_filerar('temp.txt',bk)
        except Exception as e:
            print(compressfile,e)
    if os.path.exists('temp.txt'):
        os.remove('temp.txt')
        pass
    
    return    

def read_filezip(fn,bk):        
    f=open(fn,'r')
    lines=f.readlines()
    for line in lines:
        line=line.strip()
        r=line.split('  ')
        #if len(r)==3:
        doc=r[-1]
        ftype=os.path.splitext(doc)[1]
        if len(ftype)>1:
            #fdoc=os.path.join(root,doc)
            f_write(bk,doc+'\n')
            #print(doc)
    return

def read_filerar(fn,bk):
    f=open(fn,'r')
    lines=f.readlines()
    for line in lines:
        line=line.strip()
        r=line.split('  ')
        #print(r)
        #if len(r)==3:
        doc=r[-1]
        ftype=os.path.splitext(doc)[1]
        if len(ftype)>1:
            #fdoc=os.path.join(root,doc)
            f_write(bk,doc+'\n')
            #print(doc)
    return

def book_collect(path,bk):
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
            elif fn[1] in booktype:#['.rar','zip']:
                fullpath1=os.path.join(root,f)
                line='-f %s \n'%fullpath1
                f_write(bk,line)
            elif fn[1] in ['.rar','zip']:
                fullpath=os.path.join(root,f)
                comressfile_listname(fullpath,bk)
    return
                

bk=sys.argv[2]
book_collect(path,bk)

