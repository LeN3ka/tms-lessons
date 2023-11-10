def max_num(a,b):
    if a > b:
        return a
    else:
        return b

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))

max = max_num(number_1,number_2)

print("Maximum of",number_1,"and",number_2,"is",max)