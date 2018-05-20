#python3

# construct dics
# colors[color1,color2...colorN]  colorN[node1,node2...nodeN]
from math import sqrt

def find(i,j,res,candidates):
    return

def checkbound(i,j,puzzle):
    if i == 0:
        if puzzle[0] != 'black':
            return False
    if i == 4:
        if puzzle[2] != 'black':
            return False
    if j == 0:
        if puzzle[1] != 'black':
            return False
    if j == 4:
        if puzzle[3] != 'black':
            return False

def solve(result,puzzles):
    stack = [puzzles,result[:],[0,0]]
    while stack:
        temp = stack.pop(0)
        candidate = temp[0]
        res = temp[1]
        pos = temp[2]
        
        find(pos[0],pos[1],res,candidate)









if __name__ == '__main__':
    puzzles = [color[1:-1].split(',') for color in input().split()]
    n = int(sqrt(len(puzzles)))
    result = [[[]]*n for _ in range(n)]
    result = solve(result,puzzles)
    print(result)
