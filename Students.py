records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]
students = {}



for name, grade in records:
    students[name] = students.get(name,[]) + [grade]

print(students)
  
for name in students:
    grades = students[name]
    total = 0  
    for grade in grades:
        total += grade

    average = total / len(grades)  
    print("name:", name)
    print("grades:", grades)
    print("average:", round(average, 2))
    
