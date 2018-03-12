# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if from_<=1:
        from_ = 1
    if to <= 1:
        return to

    previous = 0
    current = 1

    modList = [1]

    for _ in range(to - 1):
        previous, current = current, (previous + current) % 10
        modList.append(current)
        if modList[-2:] == [1, 0]:
            break
    time1 = to // len(modList)
    remain1 = to % len(modList)
    res1 = sum(modList) * time1 + sum(modList[:remain1])
    from_ -=1
    time2 = from_ // len(modList)
    remain2 = from_ % len(modList)


    res2 = sum(modList) * time2 + sum(modList[:remain2])

    res = (res1 - res2) % 10
    return res

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))