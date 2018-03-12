# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    modList = [1]

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m
        modList.append(current)
        if modList[-2:] == [1,0]:
            break
    n = n % len(modList)

    return modList[n-1]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
