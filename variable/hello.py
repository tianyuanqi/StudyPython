'''
变量的使用
python创建变量的规则：
    使用数字、字母、下划线构成，不能使用数字作为开头
    大小写敏感（A和a是两个不同的变量）
    不要和关键字相同（有特殊含义的单词和系统保留字）

PEP 8要求：
    用小写字母拼写，多个单词用下划线连接。
    受保护的实例属性用单个下划线开头。
    私有的实例属性用两个下划线开头。
'''

##第一个python程序

print("hello word")

'''
通过变量来进行加减乘除运算
'''
a=5
b=10.5
c="杰克马"

print("a+b=",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)

'''
在python中可以用type来对变量的类型进行检查
'''
d=1+5j
e=True
print("变量a的类型为：",type(a))
print("变量b的类型为：",type(b))
print("变量c的类型为：",type(c))
print("变量d的类型为：",type(d))
print("变量e的类型为：",type(e))

