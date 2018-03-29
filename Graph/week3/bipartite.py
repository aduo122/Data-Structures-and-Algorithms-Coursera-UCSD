#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    #initial params
    color = [0 for _ in range(len(adj))]
    visited = [0 for _ in range(len(adj))]

    # for each node in new SCC run bfs
    for start_node in range(len(adj)):
        if visited[start_node] == 0:
            queue = [start_node]
        #bfs
        while queue:
            time = len(queue)
            for _ in range(time):
                temp_node = queue.pop(0)
                #get initial color
                if color[temp_node] == 0:
                    temp_c = 1
                    color[temp_node] = temp_c
                else:
                    temp_c = color[temp_node]
                #pre procedure
                visited[temp_node] = 1
                #get child
                for end_node in adj[temp_node]:
                    if visited[end_node] == 0:
                        queue.append(end_node)
                        color[end_node] = 3 - temp_c
                    else:
                        if color[end_node] == color[temp_node]:
                            return 0
                #post procedure
                visited[temp_node] = 2
    return 1

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
    print(bipartite(adj))
