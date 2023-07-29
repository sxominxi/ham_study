# 행렬 N, M 입력 받기
N, M = map(int, input().split())

A = []
# for _ in range(N):
    # A.append(list(map(int, input().split())))

B = []
# for _ in range(N):
    # B.append(list(map(int, input().split()))) 얘네 없앤거는 입력을 동일한 코드를 두번이나 받아서 입력을 더 받으려고 해서 값이 없어서 오류가 났다.

# for i in range(N):
#     a_element =list(map(int, input().split()))
#     A.append(a_element)

# for j in range(N):
#     b_element =list(map(int, input().split()))
#     B.append(b_element)

<<<<<<< HEAD
# AB = []
=======

AB = [[0]*M for i in range(N)]
# AB = [] 이걸 쓰면은 애써 초기화해서 빈자리 둔 AB가 재정의 돼서 도루묵이 됐다, 하필이면 빈 리스트로
>>>>>>> 77bbf28721abd290ff96e51d010993fb8ab8f01a

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