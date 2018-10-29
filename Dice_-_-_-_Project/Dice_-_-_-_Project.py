import random

def main():
    print(randNum)
    print(diceSelect)



def randNum():
    x = random.randint(1,6)
    return (x)



def diceOne():
    print(' ------- ')
    print('|       |')
    print('|   *   |')
    print('|       |')
    print(' ------- ')

def diceTwo():
    print(' ------- ')
    print('|       |')
    print('|  * *  |')
    print('|       |')
    print(' ------- ')

def diceThree():
    print(' ------- ')
    print('| *     |')
    print('|   *   |')
    print('|     * |')
    print(' ------- ')

def diceFour():
    print(' ------- ')
    print('| *   * |')
    print('|       |')
    print('| *   * |')
    print(' ------- ')

def diceFive():
    print(' ------- ')
    print('| *   * |')
    print('|   *   |')
    print('| *   * |')
    print(' ------- ')

def diceSix():
    print(' ------- ')
    print('| *   * |')
    print('| *   * |')
    print('| *   * |')
    print(' ------- ')


def diceSelect():
    if randNum == 1:
        print(diceOne)
    if randNum == 2:
        print(diceTwo)
    if randNum == 3:
        print(diceThree)
    if randNum == 4:
        print(diceFour)
    if randNum == 5:
        print(diceFive)
    if randNum == 6:
        print(diceSix)

main()
