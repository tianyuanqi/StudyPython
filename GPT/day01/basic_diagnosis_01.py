print("******************开始****************")
'''
练习一：个人信息输出

定义以下变量：

姓名
年龄
身高
是否正在学习 Python

要求：

使用合适的数据类型。
打印每个变量的值。
使用 type() 打印每个变量的类型。
变量名需要符合 Python 命名规范。

不要把所有值都写成字符串。
'''

name = "yuanqi"
age = 28
height = 170
is_study_python = True
print("姓名:", name, " 变量的类型为", type(name))
print(f"年龄:{age}", " 变量的类型为", type(age))
print("身高:", height, " 变量的类型为", type(height))
print("是否在学习python:", is_study_python, " 变量的类型为", type(is_study_python))

print("**************************8分割线**********************")
'''
练习二：输入与计算

编写一个程序，让用户输入：

商品名称
商品单价
商品数量

然后计算并输出总价。

示例交互：

请输入商品名称：键盘
请输入商品单价：299.5
请输入商品数量：2
商品：键盘
购买数量：2
总价：599.0

要求：

单价允许输入小数。
数量按整数处理。
不能直接拿两个未经转换的 input() 结果进行乘法。
输出中包含商品名、数量和总价。
'''

product_name = str(input("请输入商品名称:"))
priceA = float(input("请输入单价:"))
quantity = int(input("请输入数量:"))
salary = priceA * quantity

print("商品:", product_name)
print("购买数量:", quantity)
print("总价:", salary)

'''
思考并在代码注释中回答：
通过数量应该怎样计算？
未执行数量应该怎样计算？
进度百分比应该使用什么公式？
哪些变量适合使用 int，哪个计算结果可能是 float？
'''
all_case = 80
executed_cases = 50
fail_case = 3

pass_case = executed_cases - fail_case  # 通过数量=已执行数量-失败数量
Unexecuted_cases = all_case - executed_cases  # 未执行数量=总数量-已执行数量
schedule = executed_cases / all_case  # 进度=执行数量÷总数量
pass_rate = pass_case / executed_cases  # 通过率= 通过数量/执行数量
print("通过数量:", pass_case)
print("未执数量:", Unexecuted_cases)
print("执行进度:", f"{schedule:.2%}")
print("通过率:", f"{pass_rate:.2%}")

'''
对以下问题的简短解释：
为什么 input() 的结果通常需要类型转换？
因为input默认是str类型，需要转换成其他的类型才能进行计算或比较

int 和 float 在本次练习中分别适合保存什么数据？
int适合保存商品数量，用例数量这种最小单位是1的数据
float适合保存商品价格，通过率等最小单位比1还小的数据

如果输入 "2" 和 "3" 后直接使用 +，为什么可能得到 "23"？
因为输入的2和3都是字符串，这两个进行了字符串拼接，并不是数字相加

'''
