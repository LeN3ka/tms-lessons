try:
    print(1)
    print(1/0)
    print(2)
except ZeroDivisionError as e:
    print(e)

print(3)