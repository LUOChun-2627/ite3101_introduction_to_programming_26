def purify(number):
    result = []
    for i in number:
        if i % 2 == 0:
            result.append(i)
    return result