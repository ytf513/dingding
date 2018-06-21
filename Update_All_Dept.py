# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Update_All_Dept.py}.py

@Description :更新所有人员的某些信息，比如设置手机号码显示，逻辑如下:
			1.首先由根部门获取所有子部门；2.然后遍历部门，对部门进行操作
"""

import requests
from config import Token

ACCESS_TOKEN=Token.Get_Access_Token()

def main():
	#1.递归调用获得所有子部门
	'''
	https://oapi.dingtalk.com/department/list,返回参数
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
		]
	}
	'''
	res=requests.get("https://oapi.dingtalk.com/department/list",params={"access_token":ACCESS_TOKEN,"fetch_child":"true"})
	res_json=res.json()

	err_code=res_json.get("errcode")
	if err_code == 0:
		i = 0
		for x in res_json.get("department"):
			# i = i + 1
			# # 超过次数则退出
			# if i >=10:
			# 	return
			# 更新部门属性
			isSuccess = update_dept(x.get("id"), x.get("name"))
			if isSuccess == "Success":
				print "%s:%s updated!" % (x.get("id"), x.get("name"))
	else:
		print res_json.get("errmsg")

def update_dept(dept_id,dept_name):
	'''
	https://oapi.dingtalk.com/department/update?access_token=ACCESS_TOKEN,返回参数
	{
		"errcode": 0,
		"errmsg": "ok",
		"id": 61602002
	}
   '''

	# 更新部门，开启部门属性：创建群组，自动加用户，并且包含子部门
	res = requests.post("https://oapi.dingtalk.com/department/update?access_token=%s" % ACCESS_TOKEN,
						json={"id": dept_id, "createDeptGroup": True,"autoAddUser": True,"groupContainSubDept": True})

	res = res.json()
	err_code=res.get("errcode")
	if err_code == 0:
		return "Success"
	else:
		print res.get("errmsg")
		return "Error"


if __name__ == "__main__":
	main()