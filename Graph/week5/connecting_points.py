#Uses python3
import sys
import math
import heapq

def minimum_distance(x, y):
    result = 0.
    #write your code here

    #setup parameters
    queue = [[0,x[0],y[0],0]]
    heapq.heapify(queue)
    visited = [0 for _ in range(len(x))]
    v_length = 0

    while v_length < len(visited):
        # select start heap.pop()
        temp_node = heapq.heappop(queue)
        if visited[temp_node[3]] == 1:
            continue
        result += temp_node[0]
        v_length += 1

        #calculate distance, add to heap
        for node in range(len(visited)):
            if visited[node] == 0:
                t_distance = math.sqrt((temp_node[1] - x[node])**2 + (temp_node[2] - y[node])**2)
                heapq.heappush(queue,[t_distance, x[node], y[node],node])

        #get the closest point, mark
        visited[temp_node[3]] = 1






    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
