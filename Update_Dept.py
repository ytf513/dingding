# -*-  coding:utf-8 -*-
"""
@Author       : "Alex Yean"    
@Create Date  : "2018-06-19"
@Email        : "ytf513@foxmail.com"
@Description  : Create_Dept.py
"""

import requests
from config import Token

ACCESS_TOKEN=Token.Get_Access_Token()
'''返回JSON结构：
{
    "errcode": 0,
    "errmsg": "ok",
    "id": 61602002
}
'''

#更新部门
res=requests.post("https://oapi.dingtalk.com/department/update?access_token=%s" % ACCESS_TOKEN,
                  json={"id": "68555031","createDeptGroup": False,"outerDept":True})

res_json=res.json()
print res.text
#
# err_code=res_json.get("errcode")
# if err_code == "0":
# 	print res_json.get("errmsg")
# else:
# 	for x in res_json.get("department"):
# 		print "%s:%s" % (x.get("id"),x.get("name"))