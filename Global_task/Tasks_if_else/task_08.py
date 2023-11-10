number_1 = int(input("enter first numer: "))
number_2 = int(input("enter second numer: "))
number_3 = int(input("enter third numer: "))


if number_2 >= number_1:
    if number_3 >= number_2:
        print(number_3)
    else:
        print(number_2)
else:
    if number_3 >= number_1:
        print(number_3)
    else:
        print(number_1)
