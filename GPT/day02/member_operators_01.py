allowed_roles = ["admin", "tester", "developer"]
current_role = "tester"
disabled_roles = ["guest", "blocked"]

print("当前角色是否在允许角色中：", current_role in allowed_roles)
print("当前角色是否不在禁用角色中：", current_role not in disabled_roles)
print("当前角色既在允许角色中，又不在禁用角色中：", current_role in allowed_roles and current_role not in disabled_roles)
print("admin 或 manager 是否至少有一个在允许角色中：", "admin" in allowed_roles or "manager" in allowed_roles)
print("对“当前角色有效”的最终结果使用 not 取反，得到“当前角色无效”：", not (current_role in allowed_roles))

print("——————————————————————————分割线——————————————————————————")
response_text = "login success, token generated"
status_code = 200
response_time = 920

print("响应文本中是否包含success", "success" in response_text)
print("响应文本中是否不包含 error", "error" not in response_text)
print("状态码为 200，并且响应文本包含'token'。", status_code == 200 and "token" in response_text)
print("响应时间不超过 1000，并且响应文本中不存在 failed", response_time <= 1000 and "failed" not in response_text)
print("以下任意一个情况出现时，请求存在异常：状态码不是 200,响应文本包含error,响应时间大于 1000",
      status_code == 200 and "error" in response_text and response_time<=1000)


environments=input("请输入测试环境：")
allowed_environments = ["dev", "test", "staging"]
forbidden_environments = ["prod", "production"]

print("输入环境是否在允许列表中。",environments in allowed_environments)
print("输入环境是否不在禁止列表中。",environments not in forbidden_environments )
print("输入环境是否有效：同时满足前两个条件。",
      environments in allowed_environments and environments not in forbidden_environments)
print("输入是否为空字符串。",allowed_environments =="")
print("输入是否无效（为空，或者环境不有效）：",
      allowed_environments =="" or environments not in allowed_environments or environments in forbidden_environments)

