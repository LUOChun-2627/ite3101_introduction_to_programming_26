n = [3, 5, 7]
def double_list(x):
    new_list = []  # 用新变量，不要修改x
    for i in range(0, len(x)):
        new_list.append(x[i] * 2)
    return new_list

print(double_list(n))
