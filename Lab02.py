#2.a Develop a program to read the student detalis like name usn & marksin three subjects. Display the student detalis, total marks and percentage with suitable messages.
#2.b Develop a program to read the names and year of the birth person. Display whether the person is a seniior citizen or not.

def get_student_detalis():
    name = input("Enter the name of the student: ")
    usn = input("Enter the USN of the student: ")
    marks = []
    for i in range(1,4):
        mark = float(input(f"Enter the Marks of Subject {i}: "))
        marks.append(mark)
    total_marks = sum(marks)
    percentage = (total_marks / 300) * 100

    print("\n --- Student Details --- \n")
    print(f"Name: {name}")
    print(f"USN: {usn}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage}%")

get_student_detalis()

from datetime import datetime

def senior_citizen():
    name = input("Enter the name of the person: ")
    year_of_birth = int(input("Enter the year of birth of the person: "))
    current_year = datetime.now().year
    age = current_year - year_of_birth

    print(f"\n -- {name} Detalis --")
    print(f"Age : {age}")
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Not a Senior Citizen")

senior_citizen()