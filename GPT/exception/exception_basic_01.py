try:
    number = int("abc")
except ValueError as e:
    print("数字转换失败")
    print(e)

try:
    result = 10 / 0
except ZeroDivisionError:
    print('除数不能为0')


# Q1:
# try 的作用是什么？
# A: 尝试去捕获异常，将可能出现问题的代码块放到try里面，出现异常以后可以由后续except语句去处理

# Q2:
# except 的作用是什么？
# A: 当try捕获到对应的异常内容时，执行对应except里面的内容

# Q3:
# except ValueError as e 中的 e 是什么？
# A: 捕获的异常内容

# Q4:
# 为什么不推荐直接写 except: ？
# A: 如果只写except:代表try语句里不管出现任何异常都会执行except的内容，
# 问题在于你根本不知道发生了什么错误，没办法按照对应的错误去处理或者提示