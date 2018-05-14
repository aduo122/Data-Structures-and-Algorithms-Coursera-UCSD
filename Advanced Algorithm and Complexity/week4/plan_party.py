#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def dfs(tree,vertex,parent):
    # for child in tree[vertex].children:
    #     if child != parent:
    #         dfs(tree, child, vertex)

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.

    children = vertex.children
    if not children:
        return [vertex.weight,0]
    c_withV = vertex.weight
    c_withoutV = 0
    for child in children:
        if tree[child] != parent:
            t1,t2 = dfs(tree, tree[child],vertex)
            c_withV += max(0,t2)
            c_withoutV += max(0,t1,t2)

    return [c_withV,c_withoutV]

def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    root = tree[0]
    t = dfs(tree,root,Vertex(None))
    res = max(t)
    # You must decide what to return.
    return res


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()
