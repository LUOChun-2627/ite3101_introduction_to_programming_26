n = [3, 5, 7]
def double_list(x):
    x = []
    for i in range(0, len(x)):
        x.append(x[i] * 2)
    return x

print(double_list(n))
