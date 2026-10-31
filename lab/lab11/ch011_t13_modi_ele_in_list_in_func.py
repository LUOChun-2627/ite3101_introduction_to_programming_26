def double_list(x):
    # 新建空列表保存结果
    new_list = []
    for num in x:
        new_list.append(num * 2)
    return new_list

n = [3, 5, 7]
# 调用函数并打印
print(double_list(n))
