import pytest
# from common.common_util import Common_util

def read_yaml():
    return ["mayun","mahuateng"]

@pytest.fixture(scope="function",autouse=False,params=read_yaml())
def exe_database(request):
    print("执行数据库相关操作")
    yield request.param
    print("关闭数据库连接")


class TestBlog():
    level = 12

    @pytest.mark.user_manager
    def test_login(self):
        print("登录接口")

    @pytest.mark.user_manager
    def test_pay(self,exe_database):
        print("支付接口",exe_database)
        # raise Exception  # 人为抛出异常，让用例执行失败

    @pytest.mark.user_manager
    # @pytest.mark.skip()  # 无理由跳过
    @pytest.mark.skipif(level < 10, reason="身份等级小于10级跳过")  # 当不满足条件时跳过
    def test_manager(self):
        print("管理后台接口")





