## 当前工作目录
假设当前项目结构如下<br>
```text
/Users/yuanqi/my_project/
├── main.py
├── tools/
│   └── login.py
└── test_case/
    └── login_test.json

# 其中main.py会调用login.py中的login()方法，而login方法又会读取login_test.json文件
```
### 情况一：运行main.py，
然后`main.py`调用`login.py`中的`login()`方法。<br>
假设`login()`方法写的是
```
with open("test_case/login_test.json", "r", encoding="utf-8") as file:
```
当前的工作目录就是:`/Users/yuanqi/my_project`,<br>
相对路径就是代码中显示指定的:`test_case/login_test.json`<br>
那么绝对路径（最终的查找路径）也就是当前工作目录+相对路径:
`/Users/yuanqi/my_project/test_case/login_test.json`

### 情况二:直接运行`login.py`
如果先进入tools目录，再执行login.py
```text
cd /Users/yuanqi/my_project/tools
python login.py
```

那么当前的工作目录就是`/Users/yuanqi/my_project/tools`，<br>
相对路径也就会被解析成`/Users/yuanqi/my_project/tools/test_case/login_test.json`<br>
但实际并不存在这个路径，所以会出现`FileNotFoundError`

### 重点!!!,如果仍然在项目的根目录下执行`login.py`
```
cd /Users/yuanqi/my_project
python tools/login.py
```
当前的工作路径仍然是项目根目录，文件就可以正常找到


可以通过以下方式获取当前文件的父目录
```python
from pathlib import Path
Path(__file__).parent
```
## 常用的几个方法
```python
from pathlib import Path

Path.cwd()  # 当前工作目录
Path(__file__).parent  # 当前文件的父目录
Path(__file__).resolve().parent  # 当前文件所在目录的绝对路径
```
