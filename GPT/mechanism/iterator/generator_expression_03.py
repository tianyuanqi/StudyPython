numbers = [1, 2, 3, 4, 5]

list_result = [
    number * 2
    for number in numbers
]

generator_result = (
    number * 2
    for number in numbers
)

print(list_result)
print(generator_result)

print(next(generator_result))
print(next(generator_result))
print(list(generator_result))
print(list(generator_result))

# Q1:
# 列表推导式和生成器表达式
# 在结果对象上有什么主要区别？
# A: 列表推导式生成的是一个新的列表，生成器表达式生成的是一个迭代器


# Q2:
# 为什么generator_result第一次打印时
# 不是直接显示[2, 4, 6, 8, 10]？
# A:因为generator_result是一个生成器，并不是一个列表


# Q3:
# 已经执行两次next(generator_result)后，
# 再执行list(generator_result)，
# 为什么只会得到剩余的数据？
# A: 因为生成器也是迭代器，每一次执行next都会把元素往后推进一位，
# 再执行list(generator_result)时就只能得到剩余的元素


# Q4:
# 生成器为什么通常比一次性生成大列表
# 更节省额外内存？
# A: 因为生成器是一个元素一个元素的进行推进，需要时才产生结果，如果使用生成器去进行一个判断，
# 当符合条件时终止判断，此时后面的内容将不再生成，因此相对于直接一次性生成大列表。使用生成器会更省内存