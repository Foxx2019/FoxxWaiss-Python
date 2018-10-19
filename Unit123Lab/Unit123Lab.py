def main():
    #grades = [86.8,67.6,98.9,92.1]
    num = int(input("How many grades? - "))
    grades = getGrade(num)
    average = Grade(grades)
    school = input("What school do you go to? - ")
    print(school, "Student")
    year = int(input("What grade are you in? - "))
    print("You are", Year(year))
    if 8 < year < 13:
        print("Your average grade is", average)
        print("Your letter grade is", Letter(average))

def getGrade(num):
    grades = []
    for i in range(num):
        myNum = float(input("What is the grade? - "))
        grades.append(myNum)
    return grades

def Grade(grades):
    average = 0
    for i in range(len(grades)):
        average = average + float(grades[i])
    return average/len(grades)

def Year(year):
    if year == 9:
        strYear = "a Freshman"
    elif year == 10:
        strYear = "a Sophomore"
    elif year == 11:
        strYear = "a Junior"
    elif year == 12:
        strYear = "a Senior"
    else:
        strYear = "not in high school"
    return strYear

def Letter(average):
    if average > 90:
        letterGrade = "A"
    elif average > 80:
        letterGrade = "B"
    elif average > 70:
        letterGrade = "C"
    elif average > 60:
        letterGrade = "D"
    elif 0 <= average < 59:
        letterGrade = "F"
    else:
        letterGrade = "Please enter valid numbers"
    return letterGrade

main()
