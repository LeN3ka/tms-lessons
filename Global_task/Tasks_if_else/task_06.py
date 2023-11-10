date_of_the_month = int(input("enter date of the month: "))

if 3 <= date_of_the_month <= 5:
    print('it is spring')
elif 6 <= date_of_the_month <= 8:
    print('it is summer')
elif 9 <= date_of_the_month <= 11:
    print('it is autumn')
elif date_of_the_month < 1 or date_of_the_month > 12:
    print('there is no such month, enter a number from 1 to 12')
else:
    print('it is winter')