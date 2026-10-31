n = [3, 5, 7]
def double_list(x):
    new_x = []
    for i in range(0, len(x)):
        new_x.append(x[i] * 2)
    return new_x

print(double_list(n))
