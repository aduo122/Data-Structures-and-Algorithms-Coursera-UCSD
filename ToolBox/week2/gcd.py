# Uses python3
import sys

def gcd_naive(a, b):
    if a>=b:
        a,b = b,a
    while a != 0 and b != 0:
        b = b%a
        a,b = b,a
    return b

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
