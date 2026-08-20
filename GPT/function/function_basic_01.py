print("———————————————定义一个输出helly python的方法，然后调用两次———————————————————")
def say_hello():
    print("Hello Python")

say_hello()
say_hello()

print("—————————————————分割线，定义一个求和的函数———————————————————")


def add(a, b):
    return a + b
result = add(10, 20)
print(f"计算结果:{result}")

print("—————————————————分割线，定义检查状态码的函数———————————————————")
# 规则：status_code == 200 → 返回 True，其他 → 返回 False
# 调用status_pass = check_status(200)
# 然后
# if status_pass:
#     print("状态码检查通过")
# else:
#     print("状态码检查失败")
def check_status(status_code):
    if status_code == 200:
        return True
    else:
        return False

status_pass = check_status(200)
if status_pass:
    print("状态码检查通过")
else:
    print("状态码检查失败")

# Q1: 定义函数和调用函数有什么区别？
# A: 定义函数只是定义功能，并没有开始执行，只有在调用函数之后才会开始执行

# Q2: print 和 return 有什么区别？
# A: print是直接在控制台打印内容，return是函数的返回的内容，可以把返回值赋值给变量

# Q3: 一个函数没有写 return，默认返回什么？
# A: 默认返回None