fruits = ['banana', 'apple', 'orange']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')  # (It actually is.)
        break
    print('A', f)
else:
    print('A fine selection of fruits!')
