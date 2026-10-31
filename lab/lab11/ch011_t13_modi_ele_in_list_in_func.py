def double_list(x):
    new_list = []
    for num in x:
        new_list.append(num * 2)
    return new_list

n = [12, 20, 28]

# 这里直接打印 n，而不是 double_list(n)！
print(n)
