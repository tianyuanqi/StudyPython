import json

with open("user.json", "r", encoding="utf-8") as file:
    user = json.load(file)
    print(user)
    print(type(user))

    print(user["username"])
    print(user["role"])
    print(user["enabled"])

# Q1:
# json.load() 主要用来做什么？
# A: 用来加载读取整个json文件

# Q2:
# 这个 user.json 最外层是 {}，
# json.load() 后通常得到什么 Python 类型？
# A: 字典类型

# Q3:
# JSON 中 true 读取到 Python 后是什么？
# A: True