# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s) + 1
    n = len(t) + 1
    dic = {}

    for i in range(m):
        for j in range(n):
            if i == 0:
                dic[(i,j)] = j
                continue
            if j == 0:
                dic[(i,j)] = i
                continue
            else:
                if s[i-1] == t[j-1]:
                    dic[(i, j)] = min(dic[(i-1,j)]+1,dic[(i-1,j-1)],dic[(i,j-1)]+1)
                else:
                    dic[(i, j)] = min(dic[(i-1,j)]+1,dic[(i,j-1)]+1)

    return dic[(m-1,n-1)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
