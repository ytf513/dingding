# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{GetAccess}.py

@Description :获取钉钉授权

"""

import requests

CORPSECRET	 = "**"
CORPID	  	 = "**"
ACCESS_TOKEN = ""

res=requests.get("https://oapi.dingtalk.com/gettoken",params={"corpid":CORPID,"corpsecret":CORPSECRET})

res_json=res.json()
print res_json

error_code=res_json.get("errcode")

if error_code != 0:
	print res_json.get("errmsg")
else:
	ACCESS_TOKEN=res_json.get("access_token")

print ACCESS_TOKEN


