import math
from math import floor

sqrt_result = math.sqrt(81)
print(sqrt_result)

print(math.ceil(3.2))
print(floor(3.8))

# Q1: 什么是Python模块？
# A: 一个.py文件就是一个模块，把模块化代码更方便调用

# Q2:
# import math 后，
# 为什么调用 sqrt 时要写 math.sqrt()？
# A: 因为导入的是math模块，math.sqrt() 表示调用math模块里面的sqrt()函数

# Q3:
# import math
# 和
# from math import sqrt
# 有什么区别？
# A: import marh代表导入整个math.py文件，from math import sqrt代表只导入math文件中的sqrt方法