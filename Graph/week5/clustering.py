#Uses python3
import sys
import math
import heapq

def clustering(x, y, k):
    #write your code here
    if k == 0:
        return "very big"
    #setup
    queue = [[0,x[0],y[0],0]]
    visited = [0 for _ in range(len(x))]
    edge = []
    heapq.heapify(queue)
    #get tempnode, heap.pop()
    while len(edge) < len(x):
        temp = heapq.heappop(queue)
        if visited[temp[3]] == 1:
            continue

        #get distance of end nodes, if not visited, add to heapq
        for node in range(len(x)):
            if visited[node] == 1:
                continue
            temp_distance = math.sqrt((temp[1] - x[node])**2 + (temp[2] - y[node])**2)
            heapq.heappush(queue,[temp_distance,x[node],y[node],node])
        #visit the node, add edge to result
        visited[temp[3]] = 1
        edge.append(temp[0])

    edge.sort(reverse=True)
    return edge[k-2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
