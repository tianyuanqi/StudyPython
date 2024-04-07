
class Common_util:

    def setup_class(self):
        print("每个方法前执行一次")

    def teardown_class(self):
        print("每个方法后执行一次")

    def setup_method(self):
        print("每个用例前执行一次")

    def teardown_method(self):
        print("每个用例后执行一次")