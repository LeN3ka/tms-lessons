list = [int(i) for i in input('enter numbers by a space: ').split()]

zero = False
for i in list:
    if i == 0:
        print('Yes')
    else:
        print('No')