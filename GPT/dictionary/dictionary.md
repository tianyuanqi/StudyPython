
## 字典是什么。
字典是可变数据类型，用于存放键值对
与之间的列表和元组不同，字典通过"key"来访问"value"，而不是通过索引
* 字典的value可以是不同类型的
* 在同一个字典中，key必须唯一

## 创建字典
```python
# 创建字典并直接赋值
data_a = { 
    "status_code": 200,
    "message": "success"
}

data_b = {} #创建一个空字典

data_c = dict() #也是创建一个空字典
```

## 键和值的含义。
键就是key，值value是实际的数据，key和value一一对应，通过key来获取对应的值<br>

### 方括号和 get() 的区别。
在有实际key的情况下，通过方括号或者get()都可以获取value
但如果不存在对应的key，使用方括号就会报错（KeyError）<br>
get方法的优势是，如果通过key获取某个值，但这个值实际并不存在时，会报错
但通过get方法获取且该值不存在时，get方法会返回None


### 获取对应的值
有两种方式可以获取字典的值
通过key来获取
```python
response_data = {
    "status_code": 200,
    "message": "login success"
}

print(response_data["status_code"]) #通过键进行访问

print(response_data["login"]) #如果该键不存在，就会报错

```

通过get()方法获取
get方法的优势是，如果通过key获取某个值，但这个值实际并不存在时，会报错
但通过get方法获取且该值不存在时，get方法会返回None

## 获取所有的键和值
```python
response_data = {
    "status_code": 200,
    "message": "login success",
    "token": "abc123"
}
```
### 获取所有的键
```python
all_keys = response_data.keys()

print(all_keys)
print(type(all_keys))
```
结果类似
```python
dict_keys(['status_code', 'message', 'token'])
<class 'dict_keys'>
```

### 获取所有的值
```python
all_values = response_data.values()

print(all_values)
print(type(all_values))
```
结果类似
```python
dict_values([200, 'login success', 'abc123'])
<class 'dict_values'>
```

### 获取所有的键值对
```python
all_items = response_data.items()

print(all_items)
print(type(all_items))
```
结果类似
```python
dict_items([
    ('status_code', 200),
    ('message', 'login success'),
    ('token', 'abc123')
])
```

items() 中的每个键值对表现为一个二元素元组：
```python
("status_code", 200)
```



### 判断该值是否存在

和列表、元组类似，直接用in 或not in进行判断<br>
* 区别是字典判断的是key是否存在，而不是value

```python
response_data = {
    "status_code": 200,
    "message": "login success"
}

print("status_code" in response_data)
print(200 not in response_data)  # 返回True，因为没有200这个key

```




## 修改数据

#### 使用update批量修改
调用字典的update()方法可对数据进行批量操作<br>
* 对于原始数据中不存在的key，直接添加进字典<br>
* 对于原始数据中已经存在的key，update则是进行修改
* update执行成功以后返回 None
```python
# 定义
response_data = {
    "status_code": 200,
    "message": "login success"
}

# 使用update批量进行修改
response_data.update({
    "environment": "test",  # 字典没有的数据，会直接添加
    "passed": True,
    "status_code": 404  # 字典已经存在的数据，则是进行修改
})
```
### 删除元素
有两种方法可以删除字典中的元素
* 调用.pop() 方法删除，会把被删除的value作为返回值
* 使用del关键字删除，不会产生返回值

```python
# 定义一个字典
response_data = {
    "method": "get",
    "status_code": 200,
    "message": "login success"
}

# 使用pop删除
pop_delete = response_data.pop("message") # 根据key去删除对应的value，并且会把该value作为返回值

# 使用del关键字删除
del response_data["method"]  # 也是根据key去删除对应的value，但不会有返回值

```

## 列表和元组的区别
列表和元组主要通过索引读取元素；
字典通过键读取值。

列表可修改；
元组不可修改；
字典可修改。