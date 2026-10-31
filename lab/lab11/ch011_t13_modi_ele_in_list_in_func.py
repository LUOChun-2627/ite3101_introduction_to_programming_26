# 思路 B：新建列表，不破坏原来的 n（更安全，也更"函数式"）
def double_list(x):
    result = []
    for item in x:
        result.append(item * 2)
    return result
    # 或者一行：return [item * 2 for item in x]