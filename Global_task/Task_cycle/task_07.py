my_dict = {'a': 23, 'b': 33, 'c': 54, 'd': 1, 'f': 17}

max_value = None
result_key = None
for key, value in my_dict.items():
    if max_value is None or value > max_value:
        max_value = value
        result_key = key

print(result_key)