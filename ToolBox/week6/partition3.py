# Uses python3
import sys
import itertools

def partition3(A):
    if len(A)<3:
        return 0
    A.sort()
    sumNumber = sum(A)

    if sumNumber % 3 != 0:
        return 0
    tempNumber = sumNumber // 3

    if A[-1] > tempNumber:
        return 0
    dic = {}
        # print (l,len(l))
    l = A[:]
    for i in range(tempNumber + 1):
        for j in range(tempNumber + 1):
            for k in range(len(l) + 1):
            # print (i,j)
                if i == 0:
                    dic[(i,j,k)] = True
                elif j == 0:
                    dic[(i, j,k)] = True
                elif k == 0:
                    dic[(i,j,k)] = False
                elif dic[(i, j, k - 1)]:
                    dic[(i, j, k)] = True
                elif i >= l[k-1]:
                    tvalue1 = dic[(i-l[k-1],j,k-1)]
                    if tvalue1 == True:
                        dic[(i, j, k)] = True
                    else:
                        dic[(i, j, k)] = False
                elif j >= l[k-1]:
                    tvalue2 = dic[(i, j-l[k-1],k-1)]
                    if tvalue2 == True:
                        dic[(i, j, k)] = True
                    else:
                        dic[(i, j, k)] = False
                else:
                    dic[(i, j, k)] = False
                # print(dic[(i,j)])

    if dic[(tempNumber,tempNumber,len(A))]:
        return 1
    return 0

    # for c in itertools.product(range(3), repeat=len(A)):
    #     sums = [None] * 3
    #     for i in range(3):
    #         sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
    #
    #     if sums[0] == sums[1] and sums[1] == sums[2]:
    #         return 1
    #
    # return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

