# python3
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

#学习一个图遍历！
class graph:
    def __init__(self, adj):
        self.SCCgroup = [0 for i in range(len(adj))]
        self.post = [0 for i in range(len(adj))]
        self.visitedList = [0 for i in range(len(adj))]
        self.clockWise = 0
        self.adj = adj
        self.SCCnumber = {}
        self.SCCclock = 0

    def explore(self, v):
        self.visitedList[v] = 1
        self.clockWise += 1
        for i in self.adj[v]:
            if self.visitedList[i] == 0:
                self.explore(i)
        self.post[v] = self.clockWise
        self.clockWise += 1

    def explore_SCC(self, v, adj):
        # print(v)
        self.visitedList[v] = 1
        self.SCCgroup[v] = 0
        self.SCCnumber[v] = self.SCCclock
        for i in adj[v]:
            if self.visitedList[i] == 0:
                self.explore_SCC(i, adj)

    def DFS_postoder(self):
        for i in range(len(self.adj)):
            if self.visitedList[i] == 0:
                self.explore(i)

    def acyclic(self, postOrder, adj):
        numberOfSCC = 0
        # Reset the visted list to use for the main graph:
        self.visitedList = [0 for i in range(len(self.adj))]
        self.SCCgroup = postOrder

        while max(self.SCCgroup) != 0:
            i = self.SCCgroup.index(max(self.SCCgroup))
            self.explore_SCC(i, adj)
            self.SCCclock += 1
            numberOfSCC += 1
        for i in range(n):
            if self.SCCnumber[i] == self.SCCnumber[i + n]:
                return None
        satList = [0 for i in range(n)]
        sortedSCCnumber = sorted(self.SCCnumber, key=self.SCCnumber.get)
        for i in sortedSCCnumber:
            if i <= n - 1 and satList[i] == 0:
                satList[i] = i + 1
            elif i > n - 1 and satList[i - n] == 0:
                satList[i - n] = n - i - 1
        return satList

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
def isSatisfiable():
    negAdj = [[] for _ in range(2*n)]
    for clause in clauses:
        c1 = clause[0]
        c2 = clause[1]
        # two nodes are same n to n`
        if c1 == c2:
            if c1 >= 0:
                negAdj[c1 -1].append(n + c1 - 1)
            else:
                negAdj[n-c1-1].append(-c1-1)
            continue
        if c1 >= 0:
            if c2 >= 0:
                negAdj[c2-1].append(n+c1-1)
                negAdj[c1-1].append(n+c2-1)
            else:
                negAdj[n-c2-1].append(n+c1-1)
                negAdj[c1-1].append(-c2-1)
        else:
            if c2 >= 0:
                negAdj[c2-1].append(-c1-1)
                negAdj[n-c1-1].append(n+c2-1)
            else:
                negAdj[n-c2-1].append(-c1-1)
                negAdj[n-c1-1].append(-c2-1)
    adj = [[] for _ in range(2*n)]
    for i in range(len(negAdj)):
        for j in negAdj[i]:
            adj[j].append(i)

    t = graph(negAdj)
    t.DFS_postoder()
    return t.acyclic(t.post,adj)

result = isSatisfiable()
if result is None:
    print("UNSATISFIABLE")
else:
    print("SATISFIABLE");
    print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
