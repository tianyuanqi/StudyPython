
# 总结
可迭代对象: 常用的能被`for`循环遍历的数据都是可迭代对象<br>

迭代器: 通常可以通过 `iter()` 获取对应的迭代器，能够记住目前取值取到了哪里，并且能通过`next()`方法继续往后面取<br>
迭代器同时也是python为一个一个读取数据设计的一种统一机制/协议<br>
常见的`zip(...)`，`enumerate(...)`等方法也都是返回一个迭代器

生成器: 也属于迭代器，可以理解为对迭代器机制包装好的一种使用方式（按需生成数据）<br>



# 可迭代对象
常见的能够被for循环遍历的数据都是可迭代对象，例如`list`,`tuple`,`set`,`dict`,`str`,`range` <br>

```python
names = ["alice", "bob", "jack"]  # 这里的names就是一个可迭代对象

for name in names: # 用for循环去遍历names
    print(name)
```

# 迭代器 iterator
可以理解为：一个可以记住目前取到哪里的对象，并且能通过`next()`方法一条一条往后取数据


```python
names = ["alice", "bob", "jack"]  # 这里的names就是一个可迭代对象
iterator_names = iter(names)  # 生成一个迭代器

print(next(iterator_names))  # 打印 alice
print(next(iterator_names))  # 打印 bob
print(next(iterator_names))  # 打印 jack
# 取完以后，迭代器就用完了，此时如果再继续next，就会报错StopIteration
```
以上代码通过`iter()`方法来创建一个迭代器，如果需要访问下一个元素，就需要手动调用`next()`方法


# 可迭代对象和迭代器的区别是什么
例如`numbers = [10, 20, 30]`，numbers是一个`list`，也是一个可迭代对象 <br>
我们可以用for循环去遍历这个对象，但它并不是迭代器，所以不能使用`next()`

并且，for循环的底层也是才用了迭代器的方式进行循环遍历，不断的调用`next()`去访问下一个元素
大致等价于
```python
it = iter([1, 2, 3])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```
所以可以把迭代器理解为 <span style="color:red"><b>Python为“一个一个读取数据”设计的统一机制。</b></span> 


# 生成器
生成器本质上也是一种迭代器<br>
迭代器通常需要手动使用`iter()`方法创建，然后手动去使用`next()`方法访问下一个元素，或者使用`for`循环进行遍历
而生成器可以直接调用一个包含`yield`关键字的函数，或者生成器表达式去创建<br>

生成器不是一次性把所有结果都生成并保存下来，而是惰性生成数据，需要一个，就生成一个。<br>
这样可以：<br>
- <span style="color:red"><b>最大限度的减少额外内存占用</b></span> <br>
- <span style="color:red"><b>避免无意义的后续计算</b></span><br>
- <span style="color:red"><b>也很适合处理很大的数据序列</b></span><br>

例如这是一个列表表达式，生成1000万条数据，它会一次性生成所有数据，然后都丢进内存:
```python
data = [i for i in range(10_000_000)]
```
但如果换成生成器，这里使用生成器表达式创建:
```python
data = (i for i in range(10_000_000))
```
看起来和列表表达式差不多，区别只是列表表达式使用`[]`，而生成器表达式使用`()`
它不会一次性生成全部数据，而是在你遍历或调用 next() 时逐个生成。

