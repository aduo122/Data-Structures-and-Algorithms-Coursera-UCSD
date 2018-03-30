#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    q = [ node for node in range(len(adj))]
    dis = [10^10 for node in range(len(adj))]
    dis[0] = 0
    for _ in range(len(q)):
        for u in range(len(adj)):
            node_start = u
            for v in range(len(adj[node_start])):
                node_end = adj[node_start][v]
                if dis[node_end] > dis[node_start] + cost[u][v]:
                    dis[node_end] = dis[node_start] + cost[u][v]

    for u in range(len(adj)):
        node_start = u
        for v in range(len(adj[node_start])):
            node_end = adj[node_start][v]
            if dis[node_end] > dis[node_start] + cost[u][v]:
                return 1
    return 0

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
    print(negative_cycle(adj, cost))
