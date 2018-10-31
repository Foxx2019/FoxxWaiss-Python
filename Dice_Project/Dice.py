import random

def main():



def bigDice():
    dice = [0] * 6
    topL = ' ------- '
    blank = '|       |'
    oneL =  '| *     | '
    oneM =  '|   *   |'
    oneR =  '|     * |'
    twoM =  '| *   * |'
    one =   [topL, blank, oneM, blank, topL]
    two =   [topL, oneL, blank, oneR, topL]
    three = [topL, oneL, oneM, oneR, topL]
    four =  [topL, twoM, blank, twoM, topL]
    five =  [topL, twoM, oneM, twoM, topL]
    six =   [topL, twoM, twoM, twoM, topL]







def randInt():
    x = random.randint(0,6)
    print (x)

roleDice()
