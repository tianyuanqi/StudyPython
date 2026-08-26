import calculator

result_add = calculator.add(10, 20)
result_subtract = calculator.subtract(20, 5)
result_multiply = calculator.multiply(3, 4)

print(result_add)
print(result_subtract)
print(result_multiply)

# Q1:
# module_custom_01.py import calculator 时，
# calculator.py 中 __name__ == "__main__" 下面的代码会不会执行？
# A: 不会执行，只有在运行calculator.py文件时，才会执行它里面的"main"

# Q2:
# 为什么公共模块中的调试代码建议放在
# if __name__ == "__main__":
# 下面？
# A: 因为运行自己本文件的时候才会执行main里面的代码。其他函数调用的时候并不会执行调试代码
