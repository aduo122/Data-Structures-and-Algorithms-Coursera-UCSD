# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    valueDic = {}
    valueDic[0] = 0
    processDic = {}
    processDic[0] = -1
    i = 1
    while i < n+1:
        valueDic[i] = valueDic[i-1] + 1
        processDic[i] = i-1
        if i % 3 == 0:
            if valueDic[i/3] < valueDic[i] - 1:
                valueDic[i] = valueDic[i/3] + 1
                processDic[i] = i/3
        if i % 2 == 0:
            if valueDic[i/2] < valueDic[i] - 1:
                valueDic[i] = valueDic[i/2] + 1
                processDic[i] = i/2
        i += 1
    j = n
    while processDic[j] != -1:
        sequence.append(j)
        j = processDic[j]


    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
