with open("users.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"content的内容:{content}")
    print(f"content的类型:{type(content)}")

print("————————————使用readlines读取————————————")
with open("users.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    print(f"content的内容:{content}")
    print(f"content的类型:{type(content)}")

# Q1: read() 返回什么类型？
# A: 返回一个字符串

# Q2: readlines() 返回什么类型？
# A: 返回一个列表

# Q3:
# 为什么推荐使用 with open()，
# 而不是自己 open() 后再手动 close()？
# A: with open()在打开之后会自动关闭，如果是open之后再手动关闭的话，中间部分如果代码报错了，后面的关闭操作可能就不会执行