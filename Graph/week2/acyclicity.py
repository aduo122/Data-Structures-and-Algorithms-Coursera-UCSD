#Uses python3

import sys





def acyclic(adj):
    if len(adj) == 0:
        return 0
    visited = [0 for _ in range(len(adj))]

    def explore(node):
        visited[node] = 1
        if adj[node] == []:
            visited[node] = 2
            return False
        for end_node in adj[node]:
            if visited[end_node] == 1:
                return True
            elif visited[end_node] == 0:
                if explore(end_node):
                    return True
        visited[node] = 2
        return False

    for start_node in range(len(adj)):
        if visited[start_node] == 0:
            if explore(start_node):
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
