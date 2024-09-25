#2.a Develop a program to read the student detalis like name usn & marksin three subjects. Display the student detalis, total marks and percentage with suitable messages.
#2.b Develop a program to read the names and year of the birth person. Display whether the person is a seniior citizen or not.

'''def get_student_detalis():
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

get_student_detalis()'''

'''from datetime import datetime

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

senior_citizen()'''

from datetime import datetime

def senior_citizen():
    name = input("Enter the name of the person: ")
    day_of_birth = int(input("Enter the day of birth of the person: "))
    month_of_birth = int(input("Enter the month of birth of the person: "))
    year_of_birth = int(input("Enter the year of birth of the person: "))

    current_date = datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    current_year = current_date.year

    if year_of_birth > current_year:
        print("Invalid year of birth. Year of birth cannot be greater than the current year.")
        return

    if month_of_birth > current_month:
        age_in_years = current_year - year_of_birth - 1
    else:
        age_in_years = current_year - year_of_birth

    if day_of_birth > current_day and month_of_birth == current_month:
        age_in_years -= 1

    age_in_months = age_in_years * 12
    if month_of_birth > current_month:
        age_in_months += 12 - (month_of_birth - current_month)
    else:
        age_in_months += current_month - month_of_birth

    print(f"\n -- {name} Detalis --")
    print(f"Age in years : {age_in_years}")
    print(f"Age in months : {age_in_months}")
    if age_in_years >= 60:
        print("Senior Citizen")
    else:
        print("Not a Senior Citizen")

senior_citizen()
