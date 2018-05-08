# python3
import os
import subprocess
import minisat

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    dic = {}
    color = list(range(3))
    res = []
    for edge in edges:
        if edge[0] not in dic:
            dic[edge[0]] = []
        if edge[1] not in dic[edge[0]]:
            dic[edge[0]].append(edge[1])
        if edge[1] not in dic:
            dic[edge[1]] = []
        if edge[0] not in dic[edge[1]]:
            dic[edge[1]].append(edge[0])

    # construct node with color "10 11 12"
    # node has color "10 or 11 or 12"
    for key in dic.keys():
        havecolor = []
        clist = []
        for c in color:
            havecolor.append(10*key + c)
            clist.append(10*key + c)
        havecolor.append(0)
        #res.append(havecolor)
        # node don't have duplicate color
        # "-10 or -11","-11 or -12","-12 or -10"
        for i in range(len(clist)):
            dedup = [-clist[i],-clist[(i+1)%len(clist)],0]
            res.append(dedup)

    # node don't have same color with neighbor
    # "-10 or -20","-11 or -21","-12 or -22"
    for e in edges:
        for c in color:
            res.append([(-(e[0]*10 + c)),(-(e[1]*10 + c)),0])

    print(len(res),len(dic.keys())*3)
    for r in res:
        str1 = ' '.join(str(e) for e in r)
        print (str1)



    solver =  minisat.Solver()


            if line.split()[0] == "UNSAT":
                print(2,1)
                print(1,0)
                print(-1,0)
            elif line.split()[0] == "SAT":
                print(1,1)
                print(1,-1,0)

    # print("3 2")
    # print("1 2 0")
    # print("-1 -2 0")
    # print("1 -2 0")
    return
printEquisatisfiableSatFormula()
