# Day 9

# This is the program that will take a python dictionary that contains key as name of student and value as score of student in exam.

student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

# We have to decide that if

# Score is between 91-100 then grade should be "Outstanding"
# Score is between 81-90 then grade should be "Exceeds Expectations"
# Score is between 71-80 then grade should be "Acceptable"
# Score is lower then 70 then grade should be "Fail"

# Now make an empty dictionary name of Students_grade

Students_grade = {}

for key in student_scores:
    score = student_scores[key]
    if score >= 91 and score <= 100:
        Students_grade[key] = "Outstanding"
    elif score >= 81 and score <= 90:
        Students_grade[key] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        Students_grade[key] = "Acceptable"
    elif score < 70 and score >= 0:
        Students_grade[key] = "Fail"
    else:
        Students_grade[key] = "Invalid Score"

print(Students_grade)