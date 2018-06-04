# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Get_Dept}.py

@Description :

"""

import requests
from config import Token

ACCESS_TOKEN=Token.Get_Access_Token()
'''
返回参数
{
    "errcode": 0,
    "errmsg": "ok",
    "department": [
        {
           "id": 2,
            "name": "钉钉事业部",
            "parentid": 1,
            "createDeptGroup": true,
            "autoAddUser": true
        },
        {
            "id": 3,
            "name": "服务端开发组",
            "parentid": 2,
            "createDeptGroup": false,
            "autoAddUser": false
        }
    ]
}
'''

#递归调用获得所有子部门
res=requests.get("https://oapi.dingtalk.com/department/list",params={"access_token":ACCESS_TOKEN,"fetch_child":"true"})
res_json=res.json()

err_code=res_json.get("errcode")
if err_code == "0":
	print res_json.get("errmsg")
else:
	for x in res_json.get("department"):
		print "%s:%s" % (x.get("id"),x.get("name"))