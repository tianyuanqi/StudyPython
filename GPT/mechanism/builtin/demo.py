cases = [
    {
        "case_name": "case01",
        "priority": 3
    },
    {
        "case_name": "case02",
        "priority": 1
    },
    {
        "case_name": "case03",
        "priority": 2
    }
]

# 按照priority由小到大进行排序

sorted(
    cases,
    key=lambda case: case["priority"]
)

numbers = [1, 3, 5, 7, 9]

# 循环遍历数组，然后将数组的每个元素都*2
new_number_1 = []

for i in range(len(numbers)):
    new_number_1.append(numbers[i] * 2)
print(new_number_1)

# 这里使用列表推导式，可以达到和上面一样的效果,
new_numbers2 = [
    number * 2
    for number in numbers
]
print(new_numbers2)
