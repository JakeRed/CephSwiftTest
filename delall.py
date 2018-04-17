# -*- coding: utf-8 -*-
#!/usr/bin/python
# 删除集群所有文件
import swiftclient

user = 'testuser:swift'
key = 'd1W3DuawEpz2eKtNrVkO0Dk03M28WbKOiG7Yx0wK'

conn = swiftclient.Connection(
        user=user,
        key=key,
        authurl='http://192.168.40.95:7480/auth',
)

container_name = 'my-new-container'
conn.put_container(container_name)

for container in conn.get_account()[1]:
    print container['name']


for data in conn.get_container(container_name)[1]:
    conn.delete_object(container_name,data['name'])
    print '{0}\t delete success '.format(data['name'])
