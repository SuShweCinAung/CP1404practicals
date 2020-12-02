"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))
    grade = get_grade(score)
    print(grade)

def get_grade(score):
    if score < 0 or score > 100:
        grade = "Invalid score"
    else :
        if score >= 90:
            grade = "Excellent"
        elif score >= 50 :
            grade = "Pass"
        else :
            grade = "Bad"
    return grade

main()