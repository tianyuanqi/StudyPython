class BaseApi:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def build_url(self, path):
        return self.base_url + path


