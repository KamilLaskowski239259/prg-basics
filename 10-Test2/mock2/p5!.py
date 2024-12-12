import json

def f(years,course,average_grade):
    with open('student.json','r') as file:
        content=json.load(file)
        for student in content:
            if (
                student['years']>years and
                student['course']==course and
                student['average_grade'] >= average_grade
            ):
                i+=1
    return i
print(f(21, "statistics", 4))