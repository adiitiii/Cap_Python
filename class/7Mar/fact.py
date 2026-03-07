import sys
sys.setrecursionlimit(2000)
n = int(input("Enter num: "))


def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)

print(fact(n))