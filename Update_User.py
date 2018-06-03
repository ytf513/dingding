# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Update_User}.py

@Description :

"""


import requests
import json

ACCESS_TOKEN="**"

headers = {'Content-Type': 'application/json'}
res=requests.post("https://oapi.dingtalk.com/user/update?access_token=%s" % ACCESS_TOKEN,
				  json={'userid':"200744","isHide":"false"})

print res.text

print res.history
print res.request.headers