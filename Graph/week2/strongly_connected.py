#Uses python3

import sys

sys.setrecursionlimit(200000)

def explore(v, g, visited, order):
    if visited[v] != 0:
        return visited,order
    else:
        visited[v] = 1
        for node in g[v]:
            visited,order = explore(node,g,visited,order)
    order.append(v)
    visited[v] = 2
    return visited,order

def dfs(stack, g, visited):
    order = []
    for start_node in stack:
        if visited[start_node] == 0:
            visited, order = explore(start_node, g, visited, order)
    return order


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    if adj == [[]]:
        return 0
    #get reverse graph first
    radj = [[] for _ in range(len(adj))]
    for start_node in range(len(adj)):
        for end_node in adj[start_node]:
            radj[end_node].append(start_node)

    #first run dfs on reserve graph
    stack = [node for node in range(len(adj))]
    visited = [0 for node in range(len(adj))]
    # print (stack, radj, visited)
    order = dfs(stack, radj, visited)

    #then run explore for each resource
    visited = [0 for node in range(len(adj))]
    res = 0
    for node in order[::-1]:
        if visited[node] == 0:
            visited,order = explore(node, adj, visited,[])
            res += 1
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
