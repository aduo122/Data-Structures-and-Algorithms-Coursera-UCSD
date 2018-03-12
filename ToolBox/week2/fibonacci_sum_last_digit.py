# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    modList = [1]

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
        modList.append(current)
        if modList[-2:] == [1,0]:
            break
    time = n // len(modList)
    remain = n % len(modList)
    res = sum(modList)*time + sum(modList[:remain])
    res%=10


    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
