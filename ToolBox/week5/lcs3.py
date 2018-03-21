#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    m = len(a) + 1
    n = len(b) + 1
    l = len(c) + 1

    dic = {}
    for i in range(m):
        for j in range(n):
            for k in range(l):
                if i == 0 or j == 0 or k == 0:
                    dic[(i,j,k)] = 0
                else:
                    if a[i-1] == b[j-1] == c[k-1]:
                        dic[(i,j,k)] = dic[(i-1,j-1,k-1)] + 1
                    else:
                        dic[(i,j,k)] = max(dic[(i-1,j,k)],dic[(i,j-1,k)],dic[(i,j,k-1)])

    return dic[(m-1,n-1,l-1)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
