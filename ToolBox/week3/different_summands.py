# Uses python3
import sys
import math

def optimal_summands(n):
    summands = []
    #write your code here
    if n == 0:
        return []
    i = math.floor(math.sqrt(2*n+0.25)-1.5)
    res = list(range(1,i+1))
    if n > i * (i+1)/2:
        res.append(n-i * (i+1)//2)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
