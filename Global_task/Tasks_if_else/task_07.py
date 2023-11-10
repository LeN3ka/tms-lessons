number_1 = int(input("enter first numer: "))
number_2 = int(input("enter second numer: "))
number_3 = int(input("enter third numer: "))

count = 0

if number_1 > 0:
    count += 1
if number_2 > 0:
    count += 1
if number_3 > 0:
    count += 1

print(count)