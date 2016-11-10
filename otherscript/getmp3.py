# encoding:utf-8
"""
需要放在但前文件夹中，否在有汉语则显示找不到文件。
音频编码器名称 	描述
mp3lame 	通过LAME编码为VBR，ABR或CBR格式的MP3文件
lavc 	利用libavcodec中的一个编码器
faac 	FAAC AAC音频编码器
toolame 	MPEG音频Layer 2编码器
twolame 	基于tooLAME的MPEG音频Layer 2编码器
pcm 	未压缩的PCM音频
copy 	不要重新编码，这是复制已压缩的各桢
===================================================
是频编码器名称 	描述
lavc 	使用libavcodec中的一个是频编码器
xvid 	Xvid, MPEG-4高级简单格式(ASP)编码器
x264 	x264, MPEG-4高级视频编码(AVC), AKA H.264编码器
nuv 	nuppel视频，为一些实时程序所用
raw 	未压缩的视频桢
copy 	不要重新编码，只是复制已压缩的各桢
frameno 	用于三通道编码（不推荐）
=======================================================
容器格式名称 	描述
lavf 	由libavformat 支持的一种容器
avi 	音-视频混合
mpeg 	MPEG-1及MPEG-2节目流
rawvideo 	原始视频流（未经混合 - 只含一视频流）
rawaudio 	原始音频流（未经混合 - 只含一音频流）
=======================================================
libavformat容器名称 	描述
mpg 	MPEG-1及MPEG-2节目流
asf 	高级流格式
avi 	音-视频混合
wav 	波形音频
swf 	Macromedia Flash
flv 	Macromedia Flash视频
rm 	RealMedia
au 	SUN AU
nut 	NUT开放容器（实验中，不兼容标准）
mov 	QuickTime
mp4 	MPEG-4格式
dv 	Sony数字视频容器

"""
import os,sys,re

pf=sys.argv[1]

for (pf,dirs,files) in os.walk(pf):
    for old in files:
        if os.path.splitext(old)[1] in ['.rm','.rmvb']:
            print(old)
            mfile=os.path.splitext(old)[0]
            os.system("mencoder -oac mp3lame -ovc copy -of rawaudio %s -o \
    %s.mp3" % (old,mfile))
