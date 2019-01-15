import random
DICENUM = 8
def main():
    count = 0
    play = input('Want to play a game? (y/n)- ')
    setOfDice = constructDice()
    while(play) == 'y':
        diceSet = [0] * DICENUM
        addSets = []
        for i in range(DICENUM):
            roll = randInt()
            addSets.append(roll + 1)
            diceSet[i] = setOfDice[roll]
        dicePrint(diceSet)
        print(addSets)
        count += 1
        play = input('Wanna play a game?- ')
    print('you have played ', count, 'times')


def constructDice():
    topBottom = ' ------- '
    leftOne =   '| *     |'
    middleOne = '|   *   |'
    rightOne =  '|     * |'
    middleTwo = '| *   * |'
    empty =     '|       |'
    One =   [topBottom, empty, middleOne, empty, topBottom ]
    Two =   [topBottom, leftOne, empty, rightOne, topBottom]
    Three = [topBottom, leftOne, middleOne, rightOne, topBottom]
    Four =  [topBottom, middleTwo, empty, middleTwo, topBottom]
    Five =  [topBottom, middleTwo, middleOne, middleTwo, topBottom]
    Six =   [topBottom, middleTwo, middleTwo, middleTwo, topBottom]
    allDice = [One, Two, Three, Four, Five, Six]
    return allDice


def numberCount(countDice):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    for i in range(len(countDice)):
        if countDice[i] == 1:
            count1 += 1
        if countDice[i] == 2:
            count2 += 1
        if countDice[i] == 3:
            count3 += 1
        if countDice[i] == 4:
            count4 += 1
        if countDice[i] == 4:
            count4 += 1
        if countDice[i] == 5:
           count5 += 1
        if countDice[i] == 6:
           count6 += 1


def dicePrint(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print(allDice[side][dice], end = '\t')
        print()


def randInt():
    return random.randint(0, 5)


main()
