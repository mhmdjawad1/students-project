records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100], ["Tariq", 84],
    ["Ziad", 62], ["Jana", 97], ["Tariq", 73], ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]

class_journal = {}


for name, grade in records:
    class_journal[name] = class_journal.get(name, []) + [grade]

print(class_journal)



for name in class_journal:
    grades = class_journal[name]
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)

    print("name:", name)
    print("grades:", grades)
    print("average:", round(average, 2))


top_name = ""
top_average = 0

for name in class_journal:
    grades = class_journal[name]
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)

    if average > top_average:
        top_average = average
        top_name = name

print("The highest average in class is for",top_name,":",int(round(top_average,2)))
