import os
from pathlib import Path

print(os.getcwd()) #获取当前的工作目录
print(Path.cwd())
print(__file__)


# Q1:
# os.getcwd() / Path.cwd()
# 得到的是什么？
# A: 返回的是当前的工作目录


# Q2:
# __file__ 表示什么？
# A: 表示获取当前模块文件的路径（可能是相对路径，也可能是绝对路径，取决于运行方式）


# Q3:
# 当前工作目录和当前py文件所在目录
# 一定是同一个目录吗？
# A: 不一定


# Q4:
# open("user.json") 这种相对路径
# 默认主要依据什么位置去查找？
# A: 主要以当前工作目录（cwd）查找，找到该文件处于同级别目录下的"user.json"