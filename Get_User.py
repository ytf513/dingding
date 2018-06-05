# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Get_User}.py

@Description :获得该部门的员工

"""

import requests
from config import Token

ACCESS_TOKEN=Token.Get_Access_Token()

#获得部门下的员工，不包含子部门的员工
res=requests.get("https://oapi.dingtalk.com/user/simplelist",params={"access_token":ACCESS_TOKEN,"department_id":"66462421"})
res = res.json()
userlist = res.get("userlist")
for x in userlist:
	print x.get("userid"),x.get("name")
