# -*- coding: utf-8 -*-
#!/usr/bin/python
# 测试下载视频 运行格式 python downloadvideo.py 文件测试个数

import swiftclient
import datetime
import time
import sys

# TODO swift info
user = 'testuser:swift'
key = 'd1W3DuawEpz2eKtNrVkO0Dk03M28WbKOiG7Yx0wK'
rootdir = "/home/ml/uploadfile/video"
downloaddir = "/home/ml/uploadfile/download/video"

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
def downloadFile(num):
    if not num.isdigit():
        print('please input number')
        return
    num = int(num)
    start = datetime.datetime.now()
    # read all file
    f = open(rootdir + '/video.txt', 'r')
    file_names = f.readlines()
    # Guarantee not to cross the border
    for i in range(num):
        filepath = downloaddir + '/' + time.time().__str__() + file_names[i % len(file_names)].strip('\n')
        obj_tuple = conn.get_object(container_name, file_names[i % len(file_names)].strip('\n'))
        with open(filepath, 'w') as ceph_file:
            ceph_file.write(obj_tuple[1])
    end = datetime.datetime.now()
    print('test download location ' + downloaddir + ' number: ' + num.__str__() + ' spend time:' + (end-start).total_seconds().__str__() + 'MS')

downloadFile(num=count)
