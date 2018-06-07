#-*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Get_User}.py

@Description :获得该部门的员工

"""

import requests
from config import Token
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

ACCESS_TOKEN=Token.Get_Access_Token()

'''
	https://oapi.dingtalk.com/user/simplelist,返回参数
	{
    "errcode": 0,
    "errmsg": "ok",
    "hasMore": false,
    "userlist": [
        {
            "userid": "zhangsan",
            "name": "张三"
        }
    ]
	} 
	'''

#获得部门下的员工，不包含子部门的员工
res=requests.get("https://oapi.dingtalk.com/user/simplelist",params={"access_token":ACCESS_TOKEN,"department_id":"664624211"})
res = res.json()
errcode=res.get("errcode")

if errcode == 0:
	print "获取信息：%s" % res.get("errmsg")
	userlist = res.get("userlist")
	for x in userlist:
		print x.get("userid"),x.get("name")
else:
	print res.get("errcode"),res.get("errmsg")