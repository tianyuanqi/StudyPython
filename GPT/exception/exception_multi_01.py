def calculate(value):
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        print("数字格式错误请输入数字")

    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print(f"计算成功，结果为:{result}")
    finally:
        print("处理结束")

calculate("20")
calculate("abc")
calculate("0")

# Q1:
# else 在什么情况下执行？
# A: 在没有发生异常时执行

# Q2:
# finally 在什么情况下执行？
# A: 不管有没有发生异常，都会执行finally