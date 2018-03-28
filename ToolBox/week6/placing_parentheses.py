# Uses python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_and_max(M, m, ops, i, j):
    minimum = float('inf')
    maximum = float('-inf')

    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], ops[k])
        b = evalt(M[i][k], m[k + 1][j], ops[k])
        c = evalt(m[i][k], M[k + 1][j], ops[k])
        d = evalt(m[i][k], m[k + 1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum

def get_maximum_value(dataset):
    digits = []
    for i in dataset[::2]:
        digits.append(int(i))
    operations = dataset[1::2]


    m = []
    M = []
    n = len(digits)
    for p in range(n):
        m.append(list(0 for q in digits))
        M.append(list(0 for q in digits))

    for p in range(n):
        m[p][p] = digits[p]
        M[p][p] = digits[p]

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            res = min_and_max(M, m, operations, i, j)
            m[i][j], M[i][j] = res
    return M[0][len(digits) - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
