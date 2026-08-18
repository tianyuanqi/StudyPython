test_cases = [
    "login",
    "register",
    "logout"
]
# 使用 range() 输出：
# 第0个测试:
# 第1个测试:
# 第2个测试:
for index in range(len(test_cases)):
    print(f"第{index}个测试:{test_cases[index]}")


print("————————————————————————分割线——————————————————————")

# 使用 enumerate() 输出：
# 第1个测试:
# 第2个测试:
# 第3个测试:

for index,app in enumerate(test_cases):
    print(f"第{index}个测试:{app}")