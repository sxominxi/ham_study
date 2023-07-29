# 최댓값

import sys
sys.stdin = open('input.txt')

# new_list = []
# for i in range(1, 10):
#     row_max = 0
#     num_list = list(map(int, input().split()))
#     for x in num_list:
#         if x >= row_max:
#             row_max = x
#     new_list.append(row_max)

# col_max = 0
# for j in new_list:
#     if j >= col_max:
#         col_max = j
# print(col_max)

# col = new_list.index(90)
# print(col, arr)

list1 = []


for i in range(1, 10):
    nums1 = list(map(int, input().split()))
    list1.append(nums1)

list2 = []
for i in list1:
    row_max = 0
    for x in i:
        if x >= row_max:
            row_max = x
    list2.append(row_max)

col_max = 0
for j in list2:
    if j >= col_max:
        col_max = j

print(col_max)
# row = nums1.index(90)
col = list2.index(col_max) + 1
print(col)




# print(list1)