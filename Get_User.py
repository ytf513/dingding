# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Get_User}.py

@Description :

"""

import requests

ACCESS_TOKEN="***"

res=requests.get("https://oapi.dingtalk.com/department/list_parent_depts",params={"access_token":ACCESS_TOKEN,"userId":"119249"})

print res.text
#res=requests.get("https://oapi.dingtalk.com/user/get_org_user_count?access_token=%s&onlyActive=%s" % (ACCESS_TOKEN,"1"))
#print res.text