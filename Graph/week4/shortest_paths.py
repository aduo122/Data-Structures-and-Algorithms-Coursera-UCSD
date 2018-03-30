#Uses python3

import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    q = [ node for node in range(len(adj))]
    distance[s] = 0
    reachable[s] = 1


    for _ in range(len(q)-1):
        visited = [0 for node in range(len(adj))]
        queue = [s]
        while queue:
            u = queue.pop(0)
            node_start = u
            if visited[u] == 0:
                for v in range(len(adj[node_start])):
                    node_end = adj[node_start][v]
                    if distance[node_end] > distance[u] + cost[u][v]:
                        distance[node_end] = distance[u] + cost[u][v]
                        reachable[node_end] = 1
                    if visited[node_end] == 0:
                        queue.append(node_end)
                visited[u] = 1


    visited = [0 for node in range(len(adj))]
    queue = [s]
    while queue:
        u = queue.pop(0)
        node_start = u
        if visited[u] == 0:
            for v in range(len(adj[node_start])):
                node_end = adj[node_start][v]
                if shortest[node_end] != 0:
                    if distance[node_end] > distance[u] + cost[u][v]:
                        distance[node_end] = distance[u] + cost[u][v]
                        shortest[node_start] = 0
                        markloop(adj,node_start,shortest)
                    if visited[node_end] == 0:
                        queue.append(node_end)
            visited[u] = 1

def markloop(adj,s,shortest):
    wait = [s]
    while wait:
        temp = wait.pop(0)
        for end in adj[temp]:
            if shortest[end] != 0:
                wait.append(end)
                shortest[end] = 0

    pass


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

