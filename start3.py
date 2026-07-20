import requests

#测试数据
test_cases = [
    {"username": "admin", "password": "123456", "expected_code": 200},
    {"username": "test_user", "password": "wrongpwd", "expected_code": 401},
    {"username": "empty_user", "password": "", "expected_code": 400}
]


#登录接口
def test_login(url, username, password):
   userdata={
       "username":username,
       "password":password
   }
   req=requests.post(url,json=userdata)
   return req.status_code


failList=[]
failcount=0
#for循环遍历测试数据，i表示每一条单独的测试账户
for i in test_cases:
    username=i["username"]
    password=i["password"]
    expected_code=i["expected_code"]

    actual_code=test_login("https://httpbin.org/post",username,password)


    try:
        assert actual_code==expected_code,f"账号{username}测试失败，预期的状态码为:{expected_code},实际的返回结果为{actual_code}"
    except AssertionError as e:
        failcount+=1
        failList.append(f"{username}报错:{e}")

print(f"测试失败的账号有{failList}")
    # if actual_code==expected_code:
    #     print(f"账号{username}测试通过")
    # else:
    #     print(f"账号{username}测试失败，预期状态码为{expected_code}，实际返回的状态码为:{actual_code}")