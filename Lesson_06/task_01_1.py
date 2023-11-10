def input_list_with_simple_cycle() -> list[int]:
    input_strings = input().split()
    input_numbers = []
    for s in input_strings:
        input_numbers.append(int(s))
    return input_numbers


def input_list_with_generator() -> list[int]:
    return [int(s) for s in input().split()]


def input_list_with_map() -> list[int]:
    return list(map(int, input().split()))


print(input_list_with_simple_cycle())
print(input_list_with_generator())
print(input_list_with_map())