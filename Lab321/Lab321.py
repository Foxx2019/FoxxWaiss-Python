def main():
    numList1 = [93.4, 86.8, 98.2, 89.9, 79.4, 94.6]
    gradeIn = input("what year are you in? - ")
    grade1 = int(gradeIn)
    print("you are " + grade(grade1))
    print("your current average score is " + str(getGradeAverage(numList1)))
    print("your current letter grade is " + str(getLetterGrade(getGradeAverage(numList1))))
    if (getLetterGrade == "A") or (getLetterGrade == "B") or (getLetterGrade == "B"):
        print("whoop whoop, you pass")


def grade(gradeIn):
    if gradeIn == 12:
        return("a senior")
    elif gradeIn == 11:
        return("a junior!")
    elif gradeIn == 10:
        return("a sophmore")
    elif gradeIn == 9:
        return("a freshman")
    else:
        return("not in highschool you silly goose!")


def getGradeAverage(numList1):
    numList1 = [93.4, 86.8, 98.2, 89.9, 79.4, 94.6]
    average = sum(numList1) / float(len(numList1))
    return(average)


def getLetterGrade(getGradeAverage):
    if getGradeAverage >= 90:
        letterGrade = ("A")
    elif getGradeAverage >= 80:
        letterGrade = ("B")
    elif getGradeAverage >= 70:
        letterGrade = ("C")
    elif getGradeAverage >= 60:
        letterGrade = ("D")
    else:
        letterGrade = ("F")
    return(letterGrade)



main()
