
old = "><"
new = "<>"
people= "><>><><>><>><<"


while True:
    print(people)
    people_new = people.replace(old, new)
    if people_new == people:
        break
    people = people_new


