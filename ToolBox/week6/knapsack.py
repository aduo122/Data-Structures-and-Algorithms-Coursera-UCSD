# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here

    dic = {}
    res = 0
    for i in range(W+1):
        for j in range(len(w)+1):
            if i == 0:
                dic[(i,j)] = True
            elif j == 0:
                dic[(i,j)] = False
            elif w[j-1] <= i:
                tvalue = i - w[j-1]
                if dic[(tvalue,j-1)] == True:
                    dic[(i,j)] = dic[(tvalue,j-1)]
                    res = i
                else:
                    dic[(i, j)] = dic[(i, j - 1)]
            else:
                dic[(i,j)] = dic[(i,j-1)]






    # def helper(Weight,weight):
    #     if (Weight,len(weight)) in dic :
    #         return dic[(Weight,len(weight))]
    #     if Weight < 0:
    #         return 0
    #     if len(weight) <1:
    #         return 0
    #
    #     noCur = helper(Weight,weight[:-1])
    #     if weight[-1] <= Weight:
    #         withCur = helper(Weight - weight[-1],weight[:-1]) + weight[-1]
    #     else:
    #         withCur = noCur
    #     dic[(Weight, len(weight))] = max(withCur,noCur)
    #     return dic[(Weight, len(weight))]
    # res = helper(W,w)
    return res


    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
