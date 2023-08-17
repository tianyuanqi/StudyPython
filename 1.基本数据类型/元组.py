
#元组tuple，和list基本类似，区别是元组中的数据不可以进行修改

a="我对钱没有兴趣"
tuple = ("123",456,a)

print(tuple[1])
tuple[1]=20 #这段代码在执行以后就会报错，因为元组不允许修改数据
print(tuple)


