# python3
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def findpath(graph,from_,to):
    queue = [from_]
    dicpath = {}
    #print(len(graph.graph))
    #print(len(graph.edges))
    while queue:
        cur = queue.pop(0)
        if cur == to:
            path = []
            min_flow = float("inf")
            while cur != from_:
                edge = graph.edges[dicpath[cur]]
                min_flow = min(min_flow,edge.capacity)
                #print(min_flow)
                path.append(dicpath[cur])
                cur = edge.u
            return path,min_flow
        for ind in graph.graph[cur]:
            temp_edge = graph.edges[ind]
            temp_to = temp_edge.v
            #if temp_to not in dicpath and temp_edge.capacity > temp_edge.flow:
            if temp_to not in dicpath and temp_edge.capacity > 0:
                queue.append(temp_to)
                dicpath[temp_to] = ind
    return False,0

def max_flow(graph, from_, to, flight_num, worker_num):
    flow = 0
    # your code goes here
    path,min_flow = findpath(graph, from_, to)
    #print(len(path),min_flow)
    arrange = [-1] * flight_num
    if path:
        for i in path[1:-1]:
            t_edge = graph.get_edge(i)
            if t_edge.u in range(flight_num):
                arrange[t_edge.u] = t_edge.v - flight_num

    while path:
        for id in path[::-1]:
            edge = graph.get_edge(id)
            edge.capacity -= min_flow
            edge_reverse = graph.get_edge(id^1)
            edge_reverse.capacity += min_flow

            graph.add_flow(id, min_flow)
        path, min_flow = findpath(graph, from_, to)
        if path:
            for i in path[1:-1]:
                t_edge = graph.get_edge(i)
                if t_edge.u in range(flight_num):
                    arrange[t_edge.u] = t_edge.v - flight_num

    return arrange



class MaxMatching:
    # change the read_data function to generate graph directly
    def read_data(self):
        flight_count, worker_count = map(int, input().split())
        vertex_count = flight_count + worker_count + 2
        edge_count = flight_count * worker_count + flight_count + worker_count
        graph = FlowGraph(vertex_count)
        for flight in range(flight_count):
            temp = input().split()
            for worker in range(worker_count):
                if int(temp[worker]) == 1:
                    graph.add_edge(flight, worker+flight_count, int(temp[worker]))
        for flight in range(flight_count):
            graph.add_edge(flight_count + worker_count, flight, 1)
        for worker in range(worker_count):
            graph.add_edge(worker + flight_count, flight_count + worker_count +1, 1)
        return graph,flight_count,worker_count

    # def read_data(self):
    #     n, m = map(int, input().split())
    #     adj_matrix = [list(map(int, input().split())) for i in range(n)]
    #     return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
                    matching[i] = j
                    busy_right[j] = True

        return matching

    def solve(self):
        # adj_matrix = self.read_data()
        # matching = self.find_matching(adj_matrix)
        graph,m,n = self.read_data()
        matching = max_flow(graph, graph.size() - 2, graph.size() - 1,m,n)
        #print(matching)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
