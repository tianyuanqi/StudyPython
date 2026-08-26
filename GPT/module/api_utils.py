def check_status(status_code):
    if status_code == 200:
        return True
    else:
        return False


def check_business(business_code):
    if business_code == 0:
        return True
    else:
        return False


def get_timeout(**kwargs):
    if kwargs:
        return kwargs
    else:
        return 5


if __name__ == "__main__":
    print("测试代码")