# 행렬 N, M 입력 받기
N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

AB =[[0]*M for i in range(N)]

for i in range(N):
    a_element =list(map(int, input().split()))
    A.append(a_element)

for j in range(N):
    b_element =list(map(int, input().split()))
    B.append(b_element)

AB = []

for i in range(N):
  for j in range(M):
    AB[i][j] = A[i][j] + B[i][j]

for i in range(N):
    print(*AB[i])

# for x in range(N):
#     for y in range(M):
#         C = map(int, input().split(','))
#         C = A[x][y] + B[x][y], A[x][y] + B[x][y], A[x][y] + B[x][y]
#         y += 1
#     x += 1
#     print(C)