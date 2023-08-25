import json

with open("person.json", "r") as file:
    content = file.read()
    person = json.loads(content)
    print(person)
