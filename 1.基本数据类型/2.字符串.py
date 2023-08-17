'''
在Python中，字符串是一种表示文本数据的数据类型。字符串被视为字符序列，可以包含字母、数字、符号等字符。
字符串是不可变的，这意味着一旦创建，其内容不能被修改，但可以通过创建新的字符串来进行操作和修改。
'''

# 字符串可以使用单引号、双引号来定义，还可以使用三引号'''和"""来创建多行字符串

a = "jack"
b = 'mayun'
c = '我从来没碰过钱\n我对钱没有兴趣'  # 字符串中可以穿插换行符
d = "I've never touched money\nI'm not interested in money"
print(type(a))
print(type(b))
print(c)
print(d)

e = """
这是一个
多行
字符串
"""
print(e)
# 创建字符串时，可以使用单引号内嵌双引号，或者双引号内嵌单引号

print('单引号内嵌套双引号，"hello word"')
print("双引号内嵌套单引号，'hello word'")
'''
不能使用单引号内嵌套单引号，或者双引号内嵌套双引号这种方式来打印或使用字符串
'''
# print("双引号内嵌套双引号，"hello word"")
# print('单引号内嵌套双引号，'hello word'')
# a="双引号内嵌套双引号，"hello word""
a = "hello word"
print("a的值为:", a, ",a的地址为:", id(a))
a = "hello"
print("重新赋值以后，a的值为:", a, ",a的地址为:", id(a))

'''
字符串的操作
'''
# 通过下标来访问字符串的元素
a = "hello 你好世界"
print(a[6])

# split,将字符串切分成列表
a = "hello 你好世界"
print("切分前:", a)
b = a.split(" ")
print("切分后:", b)

# strip，去除字符串两端的空格和换行符
a = """
    这是一个字符串 
"""
print(a)
b=a.strip()
print(b)

# 字符串重复：使用乘号（*）来重复字符串多次。
a = "hello " * 3
print("字符串重复：", a)
