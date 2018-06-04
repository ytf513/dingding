# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Token}.py

@Description :获取钉钉授权Token,该文件包含重要信息：CorpSecret，防止泄漏

"""

import requests

CORPSECRET	 = "*"
CORPID	  	 = "*"

def Get_Access_Token():
	'''调用钉钉接口，获取Token
	请求方式：GET
	接口地址：https://oapi.dingtalk.com/gettoken?corpid=id&corpsecret=secrect
	返回：
	{
    "errcode": 0,
    "errmsg": "ok",
    "access_token": "fw8ef8we8f76e6f7s8df8s"
	}

	:return:Access_Token or Error
	'''

	res=requests.get("https://oapi.dingtalk.com/gettoken",params={"corpid":CORPID,"corpsecret":CORPSECRET})
	res_json=res.json()
	error_code=res_json.get("errcode")

	if error_code != 0:
		print res_json.get("errmsg")
		return "ERROR"
	else:
		return res_json.get("access_token")


if __name__ == "__main__":
	print Get_Access_Token()

