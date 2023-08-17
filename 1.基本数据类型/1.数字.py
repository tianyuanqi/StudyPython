'''

数字类型是python的常用数据类型，通常分为四种
    整数类型
    浮点型
    复数形
    布尔类型

python中所有的数字类型都是对象，是不可更改的类型，也就是说，当数字的值改变了就会产生新的对象
'''

a = 100  # int长整型
b = 1.234  # float浮点型
c = True  # boolean布尔型
d = 1 + 5j  # complex复数

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'complex'>

# number是不可变数据类型，重新赋值以后，变量的地址也会改变
a = 100
print("a的地址为:", id(a))
a = 200
print("重新赋值以后，a的地址为:", id(a))
# 在以上代码中，重新赋值会创建一个新的数字类型对象，并将变量a的引用指向这个新的对象

# 数字类型的转换
a = 100
print(a)
b = float(a)
print("将整型转换成浮点型后",b)

#将要浮点型转换成整型，会丢失精度，把小数点后面的都去掉
a = 100.78
print(a)
b = int(a)
print("将浮点型转换成整型后",b)
