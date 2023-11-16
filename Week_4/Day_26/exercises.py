import random
import pandas

#new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Allan"
letters_list = [letter for letter in name]

range_double = [n*2 for n in range(1,5)]
print(range_double)

#new_list = [new_item for item in list if test]
names = ["Alex", "Beth","Coraline","Dave","Eleanor","Freddie"]
names_list = [name for name in names if len(name) < 5]
print(names_list)

names_list = [name.upper() for name in names if len(name) > 5]
print(names_list)

#Getting a file and putting each line in a list
#with open("file1.txt") as file:
#    lines = [line.rstrip() for line in file]

#with open("file1.txt") as file:
#    list1 = file1.readlines()

#result = [int(num) for num in lines1 if num in lines2]

#Dictionary Comprehension
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)

student_dict = {
    "student": ["Angela","James","Lily"],
    "score": [56,76,98]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)