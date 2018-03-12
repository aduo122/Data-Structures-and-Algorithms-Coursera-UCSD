# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    num1 = 0
    num2 = 1
    for i in range(1,n):
        num1 = num1 + num2
        num1,num2 = num2,num1
    return num2

n = int(input())
print(calc_fib(n))
