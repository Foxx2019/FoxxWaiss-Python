def schoolTimes():
    print('I go to Bellarmine Prep')
    print('My favorite subject is Science')

schoolTimes()


def howManyYears():
    x = input('what year of school are you in?')
    y = int(x) - 1
    print(str(y))

howManyYears()


def cityGrade():
    print ('you live in ' + city + ' and are in grade ' + grade)

city = input("what city are you from? ")
grade = input("what grade are you in? ")

cityGrade()


from random import *

def randomNumber():
    x = input("what is my start value? ")
    y = input("what is my end value ")
    myNumber = randint(int(x), int(y))
    print(myNumber)

randomNumber()


def boxArea(num1, num2):
    num3 = int(num1) * int(num2)
    return(num3)



def boxPer(num1, num2):
    num3 = int(num1)*2 + int(num2)*2
    return(num3)

oneNumber = input("enter a length ")
twoNumber = input("enter a width ")
threeNumber = boxArea(oneNumber, twoNumber)
print("the area is " + str(threeNumber))

Perimeter = boxPer(oneNumber, twoNumber)
print("the perimeter is " + str(Perimeter))




