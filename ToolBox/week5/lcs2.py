#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    m = len(a) + 1
    n = len(b) + 1

    dic = {}
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dic[(i,j)] = 0
            else:
                if a[i-1] == b[j-1]:
                    dic[(i,j)] = dic[(i-1,j-1)] + 1
                else:
                    dic[(i,j)] = max(dic[(i-1,j)],dic[(i,j-1)])

    return dic[(m-1,n-1)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
