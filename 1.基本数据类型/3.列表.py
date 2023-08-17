
'''
列表List是python中使用最频繁的数据类型
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
'''

#这里创建了一个列表list，在里面储存了数字类型，字符串类型和变量a
a="我对钱没有兴趣"
list=[100,123.4,a,"wo"]

#list是一种可变数据类型，如果更改list里面的元素，修改的只是对其地址的引用，而list的地址并不会变化
#例如这里，先打印出list的地址，以及第一个元素的地址
print("打印原始的list",list,"list的地址为:",id(list),"list第一个元素的地址为",id(list[0])) #输出list

#在这里，将第一个元素修改为字符串"123"
list[0]="123"
#重新输出list，以及其对应的地址
print("打印修改后list",list,"list的地址为:",id(list),"list第一个元素的地址为",id(list[0])) #输出list

list=[400,300,10.24,"hello"]
print("将list全部重新赋值以后:",list,"list的地址为:",id(list),"list第一个元素的地址为",id(list[0])) #输出list



#可以使用insert方法，在列表的指定位置来插入数据
#当insert方法传入的位置超出列表的下标范围时，会自动填充到列表的最前端或者末尾
listTest=[1,2,3,"hello",4,"5"]
print(listTest)
listTest.insert(-20,"hhh")
print(listTest)