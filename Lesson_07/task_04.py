import json

data = {'name': 'Nikita', 'surname': 'Le', 'age': '19'}

with open('file_04.json', 'w') as file:
    json.dump(data, file)
