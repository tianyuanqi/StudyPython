


## range()函数
用来生成数字序列
例如
```python
for i in range(5):
    print(i)

# 结果
# 0
# 1
# 2
# 3
# 4
```

### range(start,end) 两个参数代表起始位置和终止位置（不包含终止位置）
```python
for i in range(2,5):
    print(i)

# 结果
# 2
# 3
# 4
```

### range(start,end,step) 两个参数代表起始位置和终止位置还有步长（不包含终止位置）
```python
for i in range(2,10,3):
    print(i)

# 结果
# 2
# 5
# 8
```

## 使用enumerate()遍历列表
当你遍历一个序列，同时又需要“下标 + 元素”时,更推荐使用enumerate()
```python
test_cases = [
    "login",
    "register",
    "logout"
]

for index,app in enumerate(test_cases):
    print(f"第{index}个测试:{app}")
```
