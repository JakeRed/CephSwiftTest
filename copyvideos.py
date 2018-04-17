# -*- coding: utf-8 -*-
#!/usr/bin/python
# 脚本根据/home/ml/uploadfile/source_video 基本文件，随机copy出10000份文件测试
import os,shutil
import random
import uuid

# TODO random File Name
def randomFileName(pathName):
    file_names = []
    for parent, dirnames, filenames in os.walk(pathName):
        file_names = filenames
    x = random.randint(0, len(file_names) - 1)
    return pathName + '/' + file_names[x]

# TODO random File Name
def copyName(pathName):
    file = pathName + '/video.txt'
    filename =  uuid.uuid1().__str__() + '.mp4'
    with open(file, 'a+') as f:
        f.write(filename + '\n')
    return pathName + '/' + filename


def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.copyfile(srcfile,dstfile)
        print "copy %s -> %s"%( srcfile,dstfile)

srcfile='/home/ml/uploadfile/source_video'
dstfile='/home/ml/uploadfile/video'

for i in range(10000):
    mycopyfile(randomFileName(srcfile),copyName(dstfile))
