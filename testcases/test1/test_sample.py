import time

import pytest


class TestBBlog:
    @pytest.mark.user_manager
    def test_login(self):
        print("111登录接口")


    def test_pay(self):
        print("222支付接口")
        raise Exception