# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    avlbW = capacity
    itemList = []
    res = round(0,4)
    if len(weights) == 0 or avlbW == 0:
        return round(0,4)
    for i in range(len(weights)):
        tlist = [weights[i],values[i],round(values[i] / weights[i],4)]
        itemList.append(tlist)
    itemList.sort(key = lambda k : k[2],reverse = True)

    while avlbW>0 and itemList:
        tItem = itemList.pop(0)
        itemW = min(tItem[0],avlbW)
        res += round(itemW * chacha[2],4)
        avlbW -= itemW

    return round(res,4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
