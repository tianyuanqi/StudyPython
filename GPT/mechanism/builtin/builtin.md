


把多个可迭代对象中相同位置的数据配对起来`zip()`
如果多个对象长度不一致，会以最短的那个对象的长度为基准进行拼接，超出部分不要了
```

```

any(),至少有一个为真，就反悔True
```python
results = [
    False,
    False,
    True
]
print(any(results)) #打印True
```
all()，和any类似，全部为真才返回True
```python


```

sorted，排序，默认按照从小到大进行排序，返回一个新的列表（并不会修改原本的列表）


列表推导式
大致可以理解为
```text
[
    对数据做什么
    for 数据 in 可迭代对象
]
```
例如，定义一个初始列表，现在需要把列表的内容×2
```python
numbers = [1, 3, 5, 7, 9]

# 循环遍历数组，然后将数组的每个元素都*2
new_number_1 = []

for i in range(len(numbers)):
    new_number_1.append(numbers[i] * 2)
print(new_number_1)

# 这里使用列表推导式，可以达到和上面一样的效果,
new_numbers2 = [
    number * 2
    for number in numbers
]
print(new_numbers2)
```

