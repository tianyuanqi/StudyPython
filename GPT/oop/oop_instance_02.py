class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def change_role(self, new_role):
        self.role = new_role


user1 = User("user01", "user")
user2 = User("user02", "tester")
print(f"user1的名称为:{user1.username}, 角色为{user1.role}")
print(f"user1的名称为:{user2.username}, 角色为{user2.role}")

user1.change_role("admin")
print(f"user1的名称为:{user1.username}, 角色为{user1.role}")
print(f"user1的名称为:{user2.username}, 角色为{user2.role}")

# Q1:
# 为什么修改 user1.role 不会同时修改 user2.role？
# A: 因为每个对象都有各自的属性，有单独的内存空间去存储，修改user1不会影响到user2

# Q2:
# change_role() 中的 self.role
# 修改的是谁的属性？
# A: 修改的是调用者的属性，user1调用该方法，就修改user1的属性