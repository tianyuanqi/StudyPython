status_code = 200
response_time = 680
token = "abc123"
error_message = None

# 如果状态码等于 200，打印：状态码检查通过

if status_code == 200:
    print("状态码检查通过")
#
# 如果响应时间不超过 500：响应时间正常  否则：响应时间过长

if response_time <= 500:
    print("响应时间正常")
else:
    print("响应时间过长")

# 判断 Token：
# 不为 None：Token存在
# 否则：Token不存在
if token != None:
    print("Token存在")
else:
    print("Token不存在")

# 判断错误信息：
# error_message is None：没有错误信息
# 否则：存在错误信息
if error_message != None:
    print("没有错误信息")
else:
    print("存在错误信息")


api_pass = (
    status_code == 200
    and response_time <= 1000
    and token is not None
    and error_message is None
)

if api_pass:
    print("接口整体通过")
else:
    print("接口整体失败")
