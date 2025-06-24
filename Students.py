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



most_consistent_student = ""
smallest_difference = 2000

for name in class_journal:
    grades = class_journal[name]


    max_grade = grades[0]
    min_grade = grades[0]

    for grade in grades:
        if grade > max_grade:
            max_grade = grade
        if grade < min_grade:
            min_grade = grade

    difference = max_grade - min_grade

    if difference < smallest_difference:
        smallest_difference = difference
        most_consistent_student= name

print("Most consistent student is", most_consistent_student,"for differnce",smallest_difference)




for name in class_journal:
    grades = class_journal[name]

    for grade in grades:
        if grade < 70:
            print("Students with at least one grade below 70 is :",name)





total = 0

for name in class_journal:
    grades = class_journal[name]
    for grade in grades:
        total += 1

print("Number of grades entered accross whole class:", total)




total = 0
count = 0

for name in class_journal:
    grades = class_journal[name]

    for grade in grades:
        total += grade
        count += 1

average = total / count
print("Overall class average:", round(average, 2))
 




