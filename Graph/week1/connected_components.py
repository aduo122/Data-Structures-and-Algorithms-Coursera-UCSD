#Uses python3

import sys


def getGroup(id, grouplist):
    if grouplist[id] == id:
        return id
    else:

        return getGroup(grouplist[id],grouplist)

def merge(id1, id2, grouplist):
    group1 = getGroup(id1,grouplist)
    group2 = getGroup(id2,grouplist)
    if group1 != group2:
        grouplist[group2] = group1

def number_of_components(adj):
    res = []
    group = [i for i in range(len(adj))]
    for node in range(len(adj)):
        for snode in adj[node]:
            if snode > node:
                merge (node, snode, group)
    for node in range(len(group)):
        res.append(getGroup(node, group))

    return len(set(res))



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
    print(number_of_components(adj))
