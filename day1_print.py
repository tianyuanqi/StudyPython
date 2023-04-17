

#输出字符串
print("hello world")

#输出数字
print(50)
print(123.4)

#输出含有运算符的表达式
print(10*30)

#同时输出数字、字符，并且将内容都输出在一行中
print("衬衫的价格为:",9,"磅",15,"便士")

#数据输出到文件中，注意点1.文件路径要存在，2，要使用file=fp。（fp这里指打开文件的变量）
#a+的含义是如果文件不存在，就新建该文件，如果文件存在，就在文件后面追加内容

fp=open("/Users/yuanqi/Documents/print.txt","a+")
print("hello",file=fp)
fp.close()

#转义字符
print("hello\nword")
print("hello\rword")
print("hello\tword")
##如果字符串中药输出一个windows目录下的文件路径，windows采用的是反斜杠，容易和转义字符起冲突
print("C:\\Users\admin")
#这里用\\代表一个反斜杠，正常输出一个文件路径的话，这么来表示
print("C:\\\\Users\\admin")

print("马云说:\"我对钱没有兴趣\"")