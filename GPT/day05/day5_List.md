## 1. 列表是什么
列表是一种可变数据类型，可以保存多个数据，例如：
```python
test_cases = ["login", "logout", "register"]
```
列表使用方括号：[ ]，列表中的每个内容称为一个元素，元素之间使用逗号分隔。

列表可以存放不同类型的数据：
```python
data = ["login", 200, True, None, 1.25]
```
实际项目中通常建议一个列表中的元素具有相近含义。
例如： 
```python
status_codes = [200, 201, 400, 404, 500]
```

## 2. 列表索引
列表索引和字符串索引规则相同。
```python
cases = ["login", "register", "logout"]
```
对应关系：

| 元素 | login | register | logout |
|:---|:---:|:---:|:---:|
| 正向索引 | 0 | 1 | 2 |
| 负向索引 | -3 | -2 | -1 |


### 读取元素
索引读取的是一个元素
```python
print(cases[0])
print(cases[-1])
```

结果分别是：
```text
login
logout
```


## 3. 列表切片
列表也支持切片：
```python
cases = ["login", "register", "logout", "profile"]
```
```python
print(cases[1:3])
#结果是一个新列表：["register", "logout"]
```
仍然遵循： 包含开始位置，不包含结束位置  
<br>
### 切片的常见写法：
```python
cases[:2]    # 前两个元素
cases[2:]    # 从索引2到结尾
cases[-2:]   # 最后两个元素
cases[::-1]  # 倒序
```
注意：

```python

cases[0]
```
得到一个元素，第一个元素是什么类型，切片得到的结果就是什么类型
```
cases[0:1]
```

得到一个列表，类型是 list。（切出了只有一个元素的列表）  
<br>

## 4. 修改列表元素
列表可以通过索引直接修改：

```python
cases = ["login", "register", "logout"]

cases[1] = "create_user"

print(cases)
```

结果：
```python
["login", "create_user", "logout"]
```

这和字符串不同,字符串是不可变数据类型，如果这样写就会报错

## 5. 添加元素

使用append( )，在列表末尾添加一个元素：
```python
cases = ["login", "logout"]
cases.append("register")
print(cases)
```
结果
```python
["login", "logout", "register"]
```

append( ) 每次添加的是一个完整元素。
```python
cases = ["login", "logout"]
cases.append(["profile", "update"])
# 这样加入的是一个列表元素，不是两个字符串。
```

### 通过insert()，在指定索引位置插入元素：

格式： 列表.insert(位置, 元素)

```python
cases = ["login", "logout"]

cases.insert(1, "register")
```

结果：
```python
["login", "register", "logout"]
```


### 通过extend( )，一次添加多个元素：
```python
cases = ["login", "logout"]
cases.extend(["register", "profile"])
```
结果：
```python
["login", "logout", "register", "profile"]
```

区别在于：
```python
cases.append(["register", "profile"])
#会把整个列表作为一个元素加入。

cases.extend(["register", "profile"])
#会把里面的两个元素分别加入。
```

## 6. 删除元素
### remove()，根据元素内容删除：
```python
cases = ["login", "register", "logout"]
cases.remove("register")
```
结果：

```python
["login", "logout"]
```
注意：
删除的是第一次出现的对应元素。
元素不存在时会报错。
### pop( )，根据索引删除，并返回被删除的元素：

```python
cases = ["login", "register", "logout"]

removed_case = cases.pop(1)

print(removed_case)
print(cases)
```
结果：
```
register
["login", "logout"]
```
省略索引时： cases.pop()，默认删除最后一个元素。

### del ，根据索引删除：

```python
cases = ["login", "register", "logout"]

del cases[1]
```
del 删除后不会返回被删除的元素。


## 8. 常用操作
举例：有以下一个列表：
```python
cases = ["login", "register", "logout"]
```
列表长度
```python
print(len(cases)) 
```
判断元素是否存在

```python
print("login" in cases)
print("delete" not in cases)
```
### count( )：统计出现次数

```python
status_codes = [200, 200, 404, 500, 200]
result = status_codes.count(200)
print(result)
# 结果：3
# count() 不会修改原列表，只返回统计结果。
```

### index( )：查找元素位置
```python
test_cases = ["login", "register", "logout"]
position = test_cases.index("register")
print(position)
# 结果：1
# 如果有多个相同元素，只返回第一次出现的位置。
# 元素不存在时，index() 会抛出 ValueError。
```

### sort( )：修改原列表

```python
response_times = [320, 85, 170, 95]

response_times.sort()

print(response_times)
# 得到从小到大的顺序
```
如果用降序排列，则使用
```python
response_times = [320, 85, 170, 95]

response_times.sort(reverse=True)
```
sort()会直接改变列表，所以不要进行赋值操作，它会直接返回一个None

### sorted()：返回新的排序结果

sorted和sort的区别在于，<br>
sorted会返回一个新的列表，原列表保持不变
```python
response_times = [320, 85, 170, 95]

sorted_times = sorted(response_times)

print(response_times)
print(sorted_times)

#降序也是同样增加 reverse=True 参数
sorted_times = sorted(response_times, reverse=True)
```

### reverse()，反转列表

反转当前列表的顺序，也是直接修改原列表
```python
test_cases = ["login", "register", "logout"]

test_cases.reverse()

print(test_cases)
# 结果
# ["logout", "register", "login"]
```

## 9. 数字列表常用函数

```python
response_times = [120, 95, 310, 180]

print(min(response_times))
print(max(response_times))
print(sum(response_times))
print(len(response_times))
#
# 分别得到： 最小值、最大值、总和、元素数量

# 如果要想计算平均值，可以这样写
average_time = sum(response_times) / len(response_times)
```
