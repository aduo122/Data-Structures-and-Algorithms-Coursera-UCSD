#Uses python3

import sys
import queue
import heapq


def distance(adj, cost, s, t):
    #write your code here
    #initialize
    max_weight = 1
    for weight in cost:
        max_weight += sum(weight)
    weight = [max_weight for _ in range(len(adj))]
    relaxed = [ 0 for _ in range(len(adj))]
    queue = [(0,s)]
    weight[s] = 0

    #bfs
    while queue:
        queue.sort()
        tempNode = queue.pop(0)[1]
        for i,end_node in enumerate(adj[tempNode]):
            if relaxed[end_node] != 2:
                tweight = cost[tempNode][i] + weight[tempNode]
                if weight[end_node] > tweight:
                    if relaxed[end_node] == 1:
                        queue.remove((weight[end_node], end_node))
                    weight[end_node] = tweight
                    queue.append((weight[end_node], end_node))
                    relaxed[end_node] = 1
                if relaxed[end_node] == 0:
                    queue.append((weight[end_node], end_node))
                    relaxed[end_node] = 1
        relaxed[tempNode] = 2
    if weight[t] < max_weight:
        return weight[t]

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
