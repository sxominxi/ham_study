import sys
t = int(input())


for _ in range(1, t+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)