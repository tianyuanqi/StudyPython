number = [10, 20, 30]
interator = iter(number)
print(interator)  # 打印

print(next(interator))  # 打印第一个元素，10
print(next(interator))  # 打印第二个元素，20
print(next(interator))  # 打印第三个元素，30

try:
    print(next(interator))  # 已经没有元素了，如果不用异常处理，就会报StopIteration
except StopIteration:
    print("迭代结束")

new_interator = iter(number)

for number in new_interator:
    print(number)

# Q1:
# numbers 是可迭代对象还是迭代器？
# A: 可迭代对象


# Q2:
# iter(numbers) 得到了什么？
# A: 生成一个迭代器，用于迭代numbers这个列表


# Q3:
# next(iterator) 的作用是什么？
# A: 访问下一个元素


# Q4:
# 为什么第四次 next(iterator)
# 会触发 StopIteration？
# A: 因为列表里面已经没有元素了，没有下一位就会触发停止


# Q5:
# for循环和 iter()/next()/StopIteration
# 之间是什么关系？
# A: for循环可以简单的理解为生成了一个迭代器，然后一直用next()去访问下一个元素，直到没有元素了就触发StopIteration停止循环