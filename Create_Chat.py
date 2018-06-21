# -*-  coding:utf-8 -*-
"""
@Author       : "Alex Yean"    
@Create Date  : "2018-06-06"
@Email        : "ytf513@foxmail.com"
@Description  : 
"""
import requests
from config import Token

ACCESS_TOKEN=Token.Get_Access_Token()

def create():
	'''
	https://oapi.dingtalk.com/user/update?access_token=%s,返回参数
	{
    "errcode": 0,
    "errmsg": "updated"
	}
	:return: 
	'''

	#更新人员设置，手机号码改为显示
	res = requests.post("https://oapi.dingtalk.com/chat/create?access_token=%s" % ACCESS_TOKEN,
						json={'name': "测试群", "owner": "136747596327253935", "useridlist": ["136747596327253935","201598","0721052223419616","054967473624162380"]})
	print res.text
	res=res.json()
	err_code=res.get("errcode")
	if err_code == 0:
		print res.get("chatid")
		return "Success"
	else:
		print "Error"

if __name__ == "__main__":
	create()