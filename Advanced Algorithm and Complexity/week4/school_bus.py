# python3
from itertools import permutations
INF = 10 ** 9

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def optimal_path(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    # print(graph)
    allS = tuple(range(1,len(graph)))
    n = len(graph)
    best_ans = INF
    best_path = []
    # dic to store {S,i}
    dic = {}

    def helper(S,i):
        if (S,i) in dic:
            return dic[((S,i))]
        if not S:
            return [0,[]]
        res = float('inf')
        res_p = []
        for node in S:
            t_S = list(S)
            t_S.remove(node)
            temp = helper(tuple(t_S),node)
            d = temp[0] + graph[i][node]
            path = temp[1]
            if d < res:
                res = d
                path.append(node)
                res_p = path
        dic[(S,i)] = [res,res_p]
        return [res,res_p]

    best_ans,best_path = helper(allS,0)
    best_ans += graph[best_path[0]][0]
    best_path = [0] + best_path


    if best_ans >= INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
