def kill(person):
    # this function will modify a provided dict.
    # not all types in python can be modified in this fashion.
    # google "mutable vs immutable" for more information.
    # the takeaway is: 
    if person['status'] == "alive":
        person['status'] = "dead"
        message = f"{person['name']} has been killed!"
    else:
        message = f"{person['name']} was already dead."
    print(message)
        
def create_person(name, status='alive', favorite_food=None):
    person = {
        "name": name,
        "status": status,
        "favorite_food": favorite_food
    }
    return person
        
people = [
    {
        'name': "billy",
        'status': "alive"
    },
    {
        'name': "angela",
        'status': "alive"
    },
    {
        'name': "samantha",
        'status': "alive"
    }
]

for person in people:
    print(person['status'])
    
for i in range(10):
    new_person = create_person(name=f"new_person_{i}", favorite_food="apples")
    # new_person = create_person(f"new_person_{i}", "apples")
    people.append(new_person)

print(len(people))

i = 0
for person in people:
    if i % 2 == 0:
        kill(person)
    i += 1

surviving_people = [person for person in people if person['status']=='alive'] # and example of list comprehension
print(f"there are {len(surviving_people)} people still alive")