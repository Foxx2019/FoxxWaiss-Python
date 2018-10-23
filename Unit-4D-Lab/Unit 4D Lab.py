def main():
    list1 = ['tooth paste', 'q-tips', 'milk']
    list2 = ['milk', 'candy', 'apples']
    list3 = ['paper', 'pencils', 'q-tips']
    shoppingCart = [list1, list2, list3]
    print(allInOne(cart))


def allInOne(cart):
    newList = []
    for list in cart:
        for item in list:
            if item not in newList:
                newList.append(item)
    return newList

main()
