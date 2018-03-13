# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort(key = lambda k : k[0])
    if len(segments) == 0:
        return [0,0]
    res = []
    c = segments[0]
    check = [c.start,c.end]

    while segments:
        temp = segments.pop(0)
        lo = max(check[0],temp.start)
        hi = min(check[1], temp.end)
        if lo <= hi:
            check[0] = lo
            check[1] = hi
        else:
            res.append(check[0])
            check[0],check[1] = temp.start,temp.end
    res.append(check[0])

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

