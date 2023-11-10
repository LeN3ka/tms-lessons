import json

data = {'name': 'Nikita', 'surname': 'Le', 'age': '19'}

with open('file_03.json', 'w') as file:
    json.dump(data, file)
