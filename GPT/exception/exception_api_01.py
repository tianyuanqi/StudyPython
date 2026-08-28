success_response = {
    "status_code": 200,
    "json": {
        "business_code": 0,
        "token": "token_abc123"
    }
}

failed_response = {
    "status_code": 200,
    "json": {
        "business_code": 0
    }
}


def extract_token(response):
    try:
        token = response["json"]["token"]
    except KeyError as e:
        print(f"接口缺少响应字段{e}")
        return None
    else:
        return token
    finally:
        print("token提取结束")


succe_token = extract_token(success_response)
print(succe_token)

failed_token = extract_token(failed_response)
print(failed_token)

# Q1:
# failed_response 中缺少 token 时，
# 为什么会出现 KeyError？
# A: 因为是根据"token"这个key来寻找内容的，找不到内容就会报keyError

# Q2:
# finally 为什么两次调用都会执行？
# A: 因为不管有没有出现异常，都会出现finally的内容

# Q3:
# 异常处理是不是应该替代所有 if 判断？
# A: 不行，异常处理只能根据是否出现异常以及异常的内容去进行捕获，并不能判断其他条件或者元素内容等，所以不能代替if