
a="我对钱没有兴趣"
list=[100,123.4,a,"wo"]
print(list)
print("list的地址为：",id(list))
print("list第一个元素的地址为",id(list[0]))

list[0]="123"
print(list)
print("对第一个元素重新赋值以后，list的地址为：",id(list))
print("对第一个元素重新赋值以后，list第一个元素的地址为",id(list[0]))
