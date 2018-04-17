# -*- coding: utf-8 -*-
#!/usr/bin/python
# 计算/home/ml/uploadfile/video 前n个文件的大小MB
import os
import sys

rootdir = "/home/ml/uploadfile/video"
count = sys.argv[1]

def getFileSize(num,size=0):
    if not num.isdigit():
        print('please input number')
        return
    num = int(num)
    f = open(rootdir + '/video.txt', 'r')
    file_names = f.readlines()
    for f in range(num):
        size += os.path.getsize(os.path.join(rootdir, file_names[f].strip('\n')))
        
    return size/(1024*1024)


print(getFileSize(num=count))
