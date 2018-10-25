def main():
    shoppingCart = [['toothpaste', "q-tips", "milk"],["milk", "candy", "apples"],["paper", "pencils", "q-tips"]]
    print(shoppingCart)
    input('pause')
    print(allInOne(shoppingCart))
    input('pause')
    print("Q-tips appear", countQtips(shoppingCart), "times")


def allInOne(cart):
    newList1 = []
    for list in cart:
#goes into the 3 lists in shoppingCart
        for item in list:
#goes into the contents of each list
            if item not in newList1:
                newList1.append(item)
#this allows only one of each item to be in newList1
    return newList1


def countQtips(cart):
    newList2 = []
    count = 0
    for list in cart:
        for item in list:
            if item not in cart:
                newList2.append(item)
    for i in range(len(newList2)):
        if newList2[i] == 'q-tips':
            count += 1
    return count


main()
