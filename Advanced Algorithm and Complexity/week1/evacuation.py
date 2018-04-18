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


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    # print(graph.get_edge(0).u,graph.get_edge(0).v,graph.get_edge(1).u,graph.get_edge(1).v)
    # print(graph.get_edge(2).u,graph.get_edge(2).v,graph.get_edge(3).u,graph.get_edge(3).v)
    # print(graph.get_edge(4).u, graph.get_edge(4).v, graph.get_edge(5).u, graph.get_edge(5).v)
    return graph

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
            while cur != 0:
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

def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    path,min_flow = findpath(graph, from_, to)
    #print(len(path),min_flow)

    while path:
        flow += min_flow
        for id in path[::-1]:
            edge = graph.get_edge(id)
            edge.capacity -= min_flow
            edge_reverse = graph.get_edge(id^1)
            edge_reverse.capacity += min_flow

            graph.add_flow(id, min_flow)
        path, min_flow = findpath(graph, from_, to)
    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
