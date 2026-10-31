n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))      # [6, 10, 14]
print(double_list(n))      # [12, 20, 28]