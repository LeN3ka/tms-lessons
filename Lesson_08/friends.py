from person import Person

from functools import reduce


def get_oldest_person(friends: list[Person] | tuple[Person]):
    if friends:
        oldest_friend = reduce(lambda x, y: x if x.age > y.age else y, friends)
        oldest_friend.print_person_info()


def filter_male_person(friends: list[Person] | tuple[Person]):
    [friend.print_person_info() for friend in friends if friend.gender == "M"]


if __name__ == "__main__":
    my_friends = [
        Person("Kirill", 21, "M"),
        Person("Nastya", 20, "F"),
        Person("Sasha", 19, "F"),
        Person("Vanya", 25, "M"),
        Person("Oleg", 33, "M")
    ]

    # Вывод всех друзей
    [friend.print_person_info() for friend in my_friends]

    # Вывод старшего друга
    print("The oldest Person: ")
    get_oldest_person(my_friends)

    # Вывод друзей мужского пола
    print("male Persons: ")
    filter_male_person(my_friends)