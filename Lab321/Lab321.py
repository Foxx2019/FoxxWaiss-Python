def main():
    gradeIn = input("what year are you in? - ")
    grade1 = int(gradeIn)
    print("you are " + grade(grade1))


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

numList = [93.4, 86.8, 98.2, 89.9, 79.4, 94.6]





main()
