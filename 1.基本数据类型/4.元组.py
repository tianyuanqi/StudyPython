# 元组tuple，和list基本类似，区别是元组中的数据不可以进行修改

a = "hello"
tuple = ("123", 456, a)

# print("打印元组的第二个元素",tuple[1])
# tuple[1] = 20  # 这段代码在执行以后就会报错，因为元组不允许修改数据
# print(tuple)

# 创建一个只有单个元素的元组，需要在括号后面加一个逗号,否则会被认为是其他的类型
my_tuple = (2,)  # 如果不加这个逗号，直接使用my_tuple = (2)，变量会被认为是int类型
print(my_tuple)
print(type(my_tuple))

my_tuple = (2, "hello", 3)
x, y, z = my_tuple
print(x)
print(y)
print(z)
