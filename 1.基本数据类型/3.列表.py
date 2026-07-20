'''
列表List是python中使用最频繁的数据类型
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
'''

# 这里创建了一个列表list，在里面储存了数字类型，字符串类型和变量a
a = "我对钱没有兴趣"
list = [100, 123.4, a, "wo"]

print("****************分割线（List是一种可变数据类型，可变的是里面的元素，本身地址不会变）**********************************")
# list是一种可变数据类型，如果更改list里面的元素，修改的只是对其地址的引用，而list的地址并不会变化
# 例如这里，先打印出list的地址，以及第一个元素的地址
print("打印原始的list", list, "list的地址为:", id(list), "list第一个元素的地址为", id(list[0]))
list[0] = "123"  # 在这里，将第一个元素修改为字符串"123"
print("打印修改后list", list, "list的地址为:", id(list), "list第一个元素的地址为", id(list[0]))
list = [400, 300, 10.24, "hello"]
print("将list全部重新赋值以后:", list, "list的地址为:", id(list), "list第一个元素的地址为", id(list[0]))

# 切片操作，list[start:end],其中start是起始索引，包含在切片中，end是终止索引，不包含在切片中的
list = [100, 123.4, 20, "wo", "giao", 897]
print("切片操作访问列表元素：", list[2:4])

# 可以使用insert方法，在列表的指定位置来插入数据
# 当insert方法传入的位置超出列表的下标范围时，会自动填充到列表的最前端或者末尾
listTest = [1, 2, 3, "hello", 4, "5"]
print("使用insert插入前的列表:", listTest)
listTest.insert(-20, "hhh")
print("使用insert插入后的列表:", listTest)

# 使用append方法将元素添加到末尾
listTest.append("桀桀桀")
print("使用append插入后的列表", listTest)

# 使用remove方法根据值来删除元素，或者使用del语句根据索引删除元素
listTest = [1, 2, 3, "hello", 4, "5", 5]
print("使用remove删除前的列表:", listTest)
listTest.remove(2)  # 传入数字2，删除列表中数字类型，值为2的元素
print(listTest)
listTest.remove("5")  # 传入字符串"5",删除列表中字符串类型，值为"5"的元素
print(listTest)

