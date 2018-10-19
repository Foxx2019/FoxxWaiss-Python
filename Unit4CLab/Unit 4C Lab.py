def main():
    draw7(7)
    input('pause')
    starsAndStripes(3,7)
    input('pause')
    incTriangle(7)
    input('pause')


def draw7(nums):
    for i in range(nums):
        starStr = ''
        for i in range(nums):
            starStr += '* '
        print(starStr)

def starsAndStripes(height, width):
    for i in range(height):
        starStr = ''
        stripStr = ''
        for j in range(width):
            starStr += '* '
            stripStr += '- '
        print(starStr)
        print(stripStr)

def incTriangle(num):
    for i in range(num):
        for j in range(i):
            print(str(i), end = '')
        print()
    for k in range(num,0,-1):
        for j in range(k):
            print(str(k), end = '')
        print()



main()
