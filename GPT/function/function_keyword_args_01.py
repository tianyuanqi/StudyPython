def login(username, password, timeout=5):
    print(f"username:{username}")
    print(f"password:{password}")
    print(f"timeout:{timeout}")


# 使用位置参数调用
login("test_user", "123456", 10)

# 使用关键字参数调用，且打乱顺序
login(timeout=10, password="123456", username="test_user")


# Q1: 位置参数根据什么确定对应关系？
# A: 根据函数定义时，和传参时的顺序来进行赋值（从左往右）

# Q2: 关键字参数根据什么确定对应关系？
# A: 根据参数名来进行对应，例如username，password等

# Q3: 为什么参数较多时，关键字参数通常可读性更好？
# A: 因为参数名过多时，传参显得更直观，代码检查时不用根据去位置人工核对