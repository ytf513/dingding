# -*- coding:utf-8 -*-

"""

@Author : "Alex Yean"

@Create Date : "2017-11-14"

@Email : "ytf513@foxmail.com"

@FileName:{Update_All_User.py}.py

@Description :更新所有人员的某些信息，比如设置手机号码显示，逻辑如下:
			1.首先由根部门获取所有子部门；2.然后遍历部门，获取部门下的成员
			3.最后遍历这些成员更新其相关属性
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
	if err_code == "0":
		print res_json.get("errmsg")
	else:
		i=0
		for x in res_json.get("department"):
			#根据部门id获取用户列表
			userlist=Get_Dept_User(x.get("id"), x.get("name"))
			#遍历用户列表更新其值
			for user in userlist:
				# i=i+1
				#超过次数则退出
				# if i>=10:
				# 	return
				#user.get("userid"),user.get("name")
				isSuccess=update_user(user.get("userid"),user.get("name"))
				if isSuccess == "Success":
					print "%s:%s updated!" % (user.get("userid"),user.get("name"))


# 2.然后遍历部门，获取部门下的成员
def Get_Dept_User(dept_id,dept_name):
	# 获得部门下的员工，不包含子部门的员工
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
	res = requests.get("https://oapi.dingtalk.com/user/simplelist",
					   params={"access_token": ACCESS_TOKEN, "department_id": dept_id})
	res=res.json()
	userlist=res.get("userlist")
	return userlist

def update_user(user_id,user_name):
	'''
	https://oapi.dingtalk.com/user/update?access_token=%s,返回参数
	{
    "errcode": 0,
    "errmsg": "updated"
	}
	:return: 
	'''

	#更新人员设置，手机号码改为显示
	res = requests.post("https://oapi.dingtalk.com/user/update?access_token=%s" % ACCESS_TOKEN,
						json={'userid': user_id, "isHide": "false"})
	res=res.json()
	err_code=res.get("errcode")
	if err_code == 0:
		return "Success"
	else:
		print res.get("errmsg")
		return "Error"


if __name__ == "__main__":
	main()