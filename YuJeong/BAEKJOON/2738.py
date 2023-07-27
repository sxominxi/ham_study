# 행렬 덧셈

N, M = map(int, input().split())

list1 = []
list2 = []

for i in range(1, N+1):
    nums1 = list(map(int, input().split()))
    list1.append(nums1)

for i in range(1, N+1):
    nums2 = list(map(int, input().split()))
    list2.append(nums2)

for i in range(N):
    for j in range(M):
        list1[i][j] = list1[i][j] + list2[i][j]

print(*list1[0])
print(*list1[1])
print(*list1[2])