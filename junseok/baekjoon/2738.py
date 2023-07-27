import sys

N, M = map(int, sys.stdin.readline().split())
matrix1 = []
matrix2 = []

for row in range(N):
    matrix1.append(list(map(int, sys.stdin.readline().split())))
for row in range(N):
    matrix2.append(list(map(int, sys.stdin.readline().split())))

for row in range(N):
    for cal in range(M):
        print(matrix1[row][cal] + matrix2[row][cal], end=' ')
    print()