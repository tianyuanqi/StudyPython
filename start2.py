import requests


def interface_test(url):
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        if data["url"] == url:
            return "状态码与返回值全部验证通过"
        else:
            return "接口调用成功，但url验证失败"
    else:
        return f"接口连接失败，返回码:{req.status_code}"


print(interface_test("https://httpbin.org/get"))

'''----------分割线----------------分割线----------------分割线----------------'''
print("----------分割线----------------")


def test_login(url):
    username=input("请输入用户名:")
    password=input("请输入密码:")
    user_data = {
        "username": username,
        "password": password
    }

    '''
    post第二个参数需要转换成json格式，如果没有进行强制转换，会被请求放到form表单里，就像老式网页一样请求头变成application/x-www-form-urlencoded
    然而现在绝大多数的接口和网页需要application/json的请求头，所以这里要进行强制转换（json=user_data）
    '''
    req = requests.post(url, json=user_data)
    if req.status_code == 200:
        return req.json()
    else:
        return f"请求失败，返回码为{req.status_code}"

print(test_login("https://httpbin.org/post"))
