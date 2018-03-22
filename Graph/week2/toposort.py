#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    if adj[x] == []:
        pass
    else:
        for end_node in adj[x]:
            # if used[end_node] == 0:
            used, order = dfs(adj, used, order,end_node)
    used[x] = 1
    if x in order:
        order.remove(x)
    order.append(x)
    return (used,order)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    if adj == []:
        return []
    for start_node in range(len(adj)):
        if used[start_node] == 0:
            used, order = dfs(adj, used, order, start_node)
    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

