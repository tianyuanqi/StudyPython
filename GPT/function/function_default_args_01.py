
# 请求地址:/login
# 超时时间:5
def send_request(url, timeout=5):
    print(f"请求地址:{url},超时时间:{timeout}")

send_request("/login")
send_request("/ota", 30)


print("————————————————————分割线————————————————————————")
def create_user(username, role="user"):
    print(f"用户名:{username},角色:{role}")

create_user("yuanqi")
create_user("admin01","admin")




# Q1: 什么是默认参数？
# A: 默认参数是函数在定义时就把参数的值写好，调用该函数时不需要特意去写传参

# Q2: 调用函数时传入了默认参数的新值，会使用哪个值？
# A: 使用新值

# Q3: 为什么没有默认值的参数通常要写在有默认值参数前面？
# A: 因为python是根据位置来传入参数，如果把有默认值的参数写在前面，在定义函数时就会出现SyntaxError