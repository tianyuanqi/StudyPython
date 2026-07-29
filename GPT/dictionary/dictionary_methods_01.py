print("———————————————————————文件二：字典增删改查—————————————————————————————————————")
# 依次完成：
# 使用 update() 批量加入：
#     {
#         "method": "POST",
#         "path": "/api/v1/user/login"
#     }

# 要求：
#     每一步操作后打印当前字典。
#     不直接重新定义整个字典来代替修改。
#     不把 update() 的返回值当作字典。
case_data = {
    "case_name": "login",
    "status_code": 200,
    "response_time": 180.5
}
# 将 "case_name" 修改为 "user_login"。
case_data["case_name"] = "user_login"
print(f"case_name修改以后:{case_data['case_name']}")

# 添加 "environment": "test"。
case_data["environment"] = "test"
print("添加environment以后:", case_data)

# 添加 "passed": True。
case_data["passed"] = True
print(f"添加passed以后:{case_data}")

# 使用 update() 批量加入：
#     {    "method": "POST",
#         "path": "/api/v1/user/login"}
case_data.update({
    "method": "POST",
    "path": "/api/v1/user/login"
})
print("批量添加以后", case_data)

# 使用 update() 将 "response_time" 修改为 165.8。
# 保存并打印 update() 的返回值。
save_update = case_data.update({
    "response_time": 165.8,
})
print("保存并打印 update() 的返回值：", save_update)
print("修改response_time以后:", case_data)

# 使用 pop("environment") 删除环境，并保存返回值。
# 打印被 pop() 删除的环境。
pop_env = case_data.pop("environment")
print("删除environment以后:", case_data)
print("被pop删除的环境是:", pop_env)

# 使用 del 删除 "passed"。
del case_data["passed"]
print("删除del以后:", case_data)

# 打印最终字典。
# 打印最终字典长度。
print(f"最终字典是{case_data}")
print(f"最终字典的长度是{len(case_data)}")

print("————————————————练习二：keys()、values()、items()——————————————————————")
api_data = {
    "method": "POST",
    "path": "/api/v1/user/login",
    "status_code": 200
}
# 分别保存打印
all_keys = api_data.keys()
print(f"所有的键：{all_keys}")

all_values = api_data.values()
print(f"所有的值：{all_values}")

all_items = api_data.items()
print(f"所有的item：{all_items}")

print("api_data的类型:",type(api_data))
print("all_keys的类型:",type(all_keys))
print("all_values的类型:",type(all_values))
print("all_items的类型:",type(all_items))

# 在注释中回答：
# Q keys() 会不会修改原字典？
# A 不会，keys() 返回的是视图类型的数据，不修改原字典

# Q values() 得到的是列表吗？
# A 不是列表，得到的是视图类型的数据，里面对应的是每个值，并不是列表

# items() 中的每个键值对表现为什么类型？
# 元组类型

# update() 会不会修改原字典？
# 会直接修改原字典

# update() 的返回值是什么？
# None

# 字典 pop() 是根据索引还是键删除？
# 是根据键来删除