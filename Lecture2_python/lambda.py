people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cho", "house": "Ravenclaw"}
]

# def f(person) :
#     return person["name"]

# people.sort(key=f)

people.sort(key= lambda person: person["name"])

print(people)
