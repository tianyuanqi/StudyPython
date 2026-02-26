import pytest


class TedstDemoBlog:

    @pytest.mark.user_manager
    def test_login(self):
        print("111登录接口")