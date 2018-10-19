def main():
    numbers = [10,20,30,40,50]
    upDown()
    print(MultiplyList(numbers))

def MultiplyList(List):
    print(List)
    for i in range(len(List)):
        List[i] *= 10
    return List

def upDown():
    for i in range(1,6):
        print(i, '+ 10 =', (i + 10))
        print(i, '* 10 =', (i * 10))

main()
