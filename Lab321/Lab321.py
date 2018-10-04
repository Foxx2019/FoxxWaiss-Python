def main():
    numList1 = [93.4, 86.8, 98.2, 89.9, 79.4, 94.6]
    gradeIn = input("what year are you in? - ")
    grade1 = int(gradeIn)
    print("you are " + grade(grade1))
    print("your current average score is " + str(getGradeAverage(numList1)))
    print("your " + str(getLetterGrade(getGradeAverage(numList1))))


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
    print(numList1)
    gTotal = 0
    for x in numList1:
        gTotal = gTotal + x
    average = gTotal / len(numList1)
    return(average)



def getLetterGrade(getGradeAverage):
    if getGradeAverage >= 90:
        return("Have an A ")
    elif getGradeAverage >= 80:
        return("Have a B")
    elif getGradeAverage >= 70:
        return("Have a C")
    elif getGradeAverage >= 60:
        return("Have a D")
    else:
        return("Have an F")





main()
