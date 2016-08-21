# encoding:utf-8
from zipfile import ZipFile
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request
from io import BytesIO
from bs4 import BeautifulSoup
import os,sys

url=sys.argv[1]

def _read_docx(url):
    """
    only can be used in python2.7,
    and can be decode error in python 3.x
    """
    if 'http://' in url:
        wordFile = urlopen(url).read()
    else:
        files=open(url,'r')
        wordFile=files.read()
        files.close()
    
    wordFile = BytesIO(wordFile)
    document = ZipFile(wordFile)
    xml_content = document.read('word/document.xml')

    try:
        wordObj = BeautifulSoup(xml_content.decode('utf-8'))
    except:
        wordObj = BeautifulSoup(xml_content.decode('gb18030'))
    textStrings = wordObj.findAll("w:t")
    for textElem in textStrings:
        print(textElem.text)
    return textElem

def _read_doc(url):
    doc_file = url
    text_file = '%s.txt' % os.path.splitext(doc_file)[0]
    os.system("catdoc %s > %s" % (doc_file, text_file))
    f = open(text_file, 'r')
    content = f.read()
    f.close()
    print (content)
    os.system('rm %s' % text_file)
    return content

def read_word_file(url):
    file_type=os.path.splitext(url)[1]
    file_type=file_type.replace('.','')
    print(file_type)
    if file_type=='doc':
        txt=_read_doc(url)
        return txt
    elif file_type=='docx':
        txt=_read_docx(url)
        return txt
    else:
        print('It is not word file')
        return

fd=read_word_file(url)    
