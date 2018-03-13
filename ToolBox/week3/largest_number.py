#Uses python3

import sys

def largest_number(a):
    #write your code here
    if len(a) == 0:
        return ""
    res = ""
    a.sort(key = lambda k:str(k)[0],reverse = True)

    curMax = 0
    curI = 0
    while a:
        curMax = 0
        for i in range(len(a)):
            if int(str(a[i])[0])<int(str(curMax)[0]):
                break
            if int(str(a[i])+str(curMax)) >=int(str(curMax) + str(a[i])):
                curMax = a[i]
                curI = i
        res+= str(curMax)
        del a[curI]

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
