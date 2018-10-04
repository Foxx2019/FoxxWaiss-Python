def main():
    huh = input('what word do you want ')
    print(huh)
    print(deVowel(huh))



def deVowel(huh):
    noVowel = ''
    for y in huh:
        if(y == 'a' or y == 'e' or y== 'i' or y == 'o' or y == 'u'):
            x = 'zzzzzz'
        else:
            noVowel = noVowel + y
    return (noVowel)




main()
