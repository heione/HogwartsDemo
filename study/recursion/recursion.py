import sys
sys.setrecursionlimit(2000)


def recursion(n):
    if n > 0:
        return n + recursion(n-1)
    return n


def a(n):
    b = 0
    for i in range(0, n+1):
        b += i
        # print(i)
    return b


print(a(10))
print(recursion(1000))
