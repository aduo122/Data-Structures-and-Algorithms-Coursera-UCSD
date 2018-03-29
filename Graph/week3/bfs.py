#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here

    #initial params
    ini_dis = len(adj) + 1
    dis = [ini_dis for _ in range(len(adj))]
    visited = [0 for _ in range(len(adj))]
    #start node
    queue = [s]
    dis[s] = 0
    d = 0

    #bfs
    while queue:
        time = len(queue)
        for _ in range(time):
            temp_node = queue.pop(0)
            for end_node in adj[temp_node]:
                if visited[end_node] == 0:
                    visited[end_node] = 1
                    queue.append(end_node)
            dis[temp_node] = d
            visited[temp_node] = 2
        d += 1

    if dis[t] < ini_dis:
        return dis[t]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
