# -*-  coding:utf-8 -*-
"""
@Author       : "Alex Yean"    
@Create Date  : "2018-06-19"
@Email        : "ytf513@foxmail.com"
@Description  : Delete_Dept
"""

import requests
from config import Token

ACCESS_TOKEN=Token.Get_Access_Token()

#删除用户
res=requests.get("https://oapi.dingtalk.com/department/delete",
                  params={"access_token":ACCESS_TOKEN,"id": "68555031"})
print res.text
