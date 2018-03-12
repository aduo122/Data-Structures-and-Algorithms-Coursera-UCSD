# Uses python3
import sys

def lcm_naive(a, b):

    num1 = a
    num2 = b
    if num1 >= num2:
        num1,num2 = num2,num1
    while num1 != 0:
        num2 = num2%num1
        num1,num2 = num2,num1

    return a*b//num2

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

