N,M = map(int, input().split())
arr_A = []
arr_B = []
arr_AB =[[0]*M for i in range(N)]
for i in range(N):
    a_element =list(map(int, input().split()))
    arr_A.append(a_element)
for j in range(N):
    b_element =list(map(int, input().split()))
    arr_B.append(b_element)
for i in range(N):
  for j in range(M):
    arr_AB[i][j] = arr_A[i][j] +arr_B[i][j]

for i in range(N):
    print(*arr_AB[i])
   