# Uses python3
import sys

def get_change(m):
    #write your code here
    valueDic = {}
    coins = [1,3,4]
    i = 1
    valueDic[0] = 0
    while i < m+1:
        tnumber = []
        for coin in coins:
            if (i - coin) in valueDic.keys():
                tnumber.append(valueDic[i-coin]+1)
        valueDic[i] = min(tnumber)
        i += 1
    return valueDic[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
