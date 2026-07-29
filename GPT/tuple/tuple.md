### 什么是元组
元组和列表类似，最大的区别是元组的内容是不可变的<br>

定义一个元组
```python
list_A=[100,"hello","world"] #这是一个列表

tuple_A=(100,"hello","world") #这是一个元组，元组和列表类似，只是用了圆括号

tuple_A=() # 括号里面什么都不写的话，就是创建一个空元组
print(type(tuple_A)) # 结果为 <class 'tuple'>

tuple_h=("hello") # 这样创建就不是元组了
print(type(tuple_h)) # 结果为 <class 'str'>

tuple_one=(100) # 这样创建也不是元组
print(type(tuple_one)) #结果为 <class 'int'>

case_name = ("login",) #单元素元组，必须在里面保留一个逗号
print(type(case_name))

case_name = (100,)
print(type(case_name))


```
元组创建完成后，其元素位置不能直接增加、删除或修改。


## 元组是不可变数据类型
```python
list_A=[100,"hello","world"] #这是一个列表
list_A[0]=200 #列表可以对列表中的任意元素进行重新赋值
print(f"修改后的列表为:{list_A}") #打印重新赋值之后的新列表

tuple_A=(100,"hello","world") #这是一个元组
tuple_A[0]=200  #执行到这里，就会报错：
# TypeError: 'tuple' object does not support item assignment
print(tuple_A)

```
