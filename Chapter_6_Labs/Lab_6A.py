def main () :
    dict = {'lol':'laughing out loud','omg':'oh my gosh','lmao':'chinese hacker'}
    d = 'y'
    while d=='y' :
        f = input("Would you like to use, modify, or view dictionary (use/mod/view) - ")
        if f=='use':
            dict = norm(dict)
        elif f=='mod':
            dict = mod(dict)
        else:
            dict = view(dict)


def norm (dict) :
    x='y'
    while x=='y' :
        d = input('Put in abbreviation - ')
        if d in dict :
            print(dict[d])
        else :
            print("This isn't in the dictionary")
            n = input("Would you like to add it? (y/n) - ")
            if n=='y' :
                c = input("What does that stand for - ")
                dict[d] = c

        x = input('Would you like to read another abreviattion (y/n) - ')
        print()
    return(dict)


def mod (dict) :
    x = 'y'
    while x=='y' :
        f = input("Would you like to remove or edit an entrey (remove/edit) - ")
        if f=='remove' :
            l = input("What abreviation would you like to remove? - ")
            del dict[l]
        elif f=='edit' :
            g = input("What abreviation would you like to edit? - ")
            q = input("What does that abreviation stand for? - ")
            del dict[g]
            dict[g] = q
        else :
            print("This ain't it, please input an r or e")
        x = input("Would you like to remove another item (y/n) - ")
        print()
    return(dict)


def view(dict) :
    for x in dict :
        print(x + ' : ' + dict[x] + '      ', end='')
    print()
    print()
    return (dict)


main()
