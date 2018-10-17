def Main () :
    myString = str(input("Enter any word - "))
    print ("Your word is - " + myString )

    print ("Your word without vowels is - " + deVowel(myString))
    print ()

    g = [0] * 4
    g [0] = float(input("Enter a number - "))
    g [1] = float(input("Enter a number - "))
    g [2] = float(input("Enter a number - "))
    g [3] = float(input("Enter a number - "))
    m = float(input("What do you want to multiply by? - "))

    print ("Your average grades using a for loop equals " + mathStuff(g , m))
    print ()



def deVowel (myString) :
    myString2 = myString
    myStringV = ""
    for x in myString2 :
        if (x == "a" or x=="e" or x=="i" or x=="o" or x=="u"or x=="A" or x=="E" or x=="O" or x=="U") :
            y = 69
        else :
            myStringV = myStringV + x
    return (myStringV)


def mathStuff (g , m) :
    Listf = [] * 4
    for x in g :
        Listf.append(float(x) * float(m))
    return (str(Listf))




Main ()
