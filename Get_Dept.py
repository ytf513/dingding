# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Get_Dept}.py

@Description :

"""

import requests

ACCESS_TOKEN="1716e17b0d503552b337f74965fc8f3a"

res=requests.get("https://oapi.dingtalk.com/department/list",params={"access_token":ACCESS_TOKEN,"fetch_child":"true"})
print res.text