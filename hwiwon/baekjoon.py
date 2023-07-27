# #2738
# N, M = map(int, input().split())

# A = []
# B = []


# for i in range(N):
#     a_num = list(map(int, input().split()))
#     A.append(a_num)
    
# for i in range(N):
#     b_num = list(map(int, input().split()))
#     B.append(b_num)

# for i in range(N):
#     for j in range(M):
#         A[i][j] += B[i][j]

# for i in A:
#     print(*i)

# #2566
# N = 9

# numbers = []

# for i in range(N):
#     A = list(map(int, input().split()))
#     for i in A:
#         numbers.append(i)

# for i in range(len(numbers)):
#     if numbers[i] == max(numbers):
#         index1 = i
#         # print (index1)

# print(max(numbers))
# print(f'{index1 // 9 + 1} {index1 % 9 + 1}')

# #10798
# lines = []
# lengths = []
# final_word = str()

# for i in range(5):
#     a = list(str(input()))
#     lines.append(a)
#     lengths += [len(a)]
    
# for i in range(max(lengths)):
#     for j in range(5):
#         current = lines[j]
#         if i <= (lengths[j] - 1):
#             final_word += current[i]
#         else:
#             final_word = final_word


# print(final_word)

# #2563

# N = int(input())

# black = []

# for i in range(N):
#     a = list(map(int, input().split()))
#     black.append(a)


# x_coordi = []
# y_coordi = []

# for i in range(len(black)):
#     x_s = list(range(black[i][0], black[i][0] + 10))
#     x_coordi.append(x_s)
    

# for i in range(len(black)):
#     y_s = list(range(black[i][1], black[i][1] + 10))
#     y_coordi.append(y_s)

# square_coordis = []

# x1 = x_coordi[i]
# y1 = y_coordi[i]

# for i in range(len(black)):
#     for j in range(10):
#         for k in range(10):
#           square_coordis.append((x_coordi[i][j], y_coordi[i][k]))

# print(len(set(square_coordis)))

