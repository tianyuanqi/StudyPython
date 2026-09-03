class ApiResponse:
    def __init__(self, status_code, business_code, data):
        self.status_code = status_code
        self.business_code = business_code
        self.data = data

    def is_success(self):
        return (
                self.business_code == 0
                and self.status_code == 200
        )
