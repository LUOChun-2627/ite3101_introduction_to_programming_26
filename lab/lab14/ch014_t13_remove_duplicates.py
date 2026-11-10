def remove_duplicates(numbers)
    result = set()
    total = []
    for i in numbers:
        if i not in result:
            result.add(i)
            total.append(i)
            