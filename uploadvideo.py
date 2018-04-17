# -*- coding: utf-8 -*-
#!/usr/bin/python
# 测试上传视频 运行格式 python uploadvideo.py 文件测试个数
import swiftclient
import os
import sys
import datetime

# TODO swift info
user = 'testuser:swift'
key = 'd1W3DuawEpz2eKtNrVkO0Dk03M28WbKOiG7Yx0wK'
rootdir = "/home/ml/uploadfile/video"
count = sys.argv[1]
# TODO container name
container_name = 'my-new-container'

#  TODO connect swift
conn = swiftclient.Connection(
        user=user,
        key=key,
        authurl='http://192.168.40.95:7480/auth',
)

# TODO uploadfile
def uploadFile(pathName,num):
    if not num.isdigit():
        print('please input number')
        return
    num = int(num)
    print('start uploading')
    start = datetime.datetime.now()
    # read all file
    f = open(rootdir + '/video.txt', 'r')
    file_names = f.readlines()
    # Guarantee not to cross the borde
    temp = len(file_names) if num > len(file_names) else num
    if temp != num:
        print('The test may be unreasonable Insufficient number of documents')
    num = temp
    for i in range(num):
        filepath = pathName + '/' + file_names[i].strip('\n')
        conn.put_object(container_name, file_names[i].strip('\n'), open(filepath, 'rb'))
    end = datetime.datetime.now()
    print('test upload location ' + pathName +  ' number: ' + num.__str__() + ' spend time:' + (end-start).total_seconds().__str__() + 'microseconds')

#  upload file 500
uploadFile(rootdir,num=count)

