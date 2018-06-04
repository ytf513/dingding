# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Get_Dept}.py

@Description :

"""

import requests
from config import KeyConfig

ACCESS_TOKEN=KeyConfig.

res=requests.get("https://oapi.dingtalk.com/department/list",params={"access_token":ACCESS_TOKEN,"fetch_child":"true"})
print res.text