from GPT.oop.demo.api_response_04 import ApiResponse
from base_api_04 import BaseApi


class LoginApi(BaseApi):
    def login(self, username, password):
        url = self.build_url("/login")
        print(f"请求地址:{url}")
        if username == "test_user" and password == "123456":
            return ApiResponse(
                status_code=200,
                business_code=0,
                data={
                    "token": "token_abc123"
                }
            )
        else:
            return ApiResponse(
                status_code=200,
                business_code=1001,
                data={}
            )
