from api_utils import check_status, check_business, get_timeout

api_result = {
    "status_code": 200,
    "business_code": 0
}

status_pass = check_status(api_result["status_code"])
code_pass = check_business(api_result["business_code"])
timeout = get_timeout(timeout=10)

if status_pass and code_pass:
    print("接口检查通过")
else:
    print("接口检查失败")
print(f"timeout:{timeout}")

print("————————————————————分割线————————————————————")
failed_result = {
    "status_code": 500,
    "business_code": 1001
}

status_pass = check_status(failed_result["status_code"])
code_pass = check_business(failed_result["business_code"])
if status_pass and code_pass:
    print("接口检查通过")
else:
    print("接口检查失败")
