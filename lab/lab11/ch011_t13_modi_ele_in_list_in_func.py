n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

# 加上这两行，预先调用两次，让n翻倍三次（初始3,5,7 → 6,10,14 →12,20,28 →24,40,56）
double_list(n)
double_list(n)

print(double_list(n))
