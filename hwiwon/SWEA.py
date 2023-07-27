# #1938

# A, B = map(int, input().split())

# if (A == 3 and B == 1):
#     print ('B')
# elif (A == 2 and B == 3):
#     print ('B')
# elif (A == 1 and B == 2):
#     print ('B')

# else :
#     print ('A')


# #2058

# num = list(input())
# num = list(map(int, num))
# sum = sum(num)
# print (sum)


# #2063

# N = int(input())
# values = list(map(int, input().split()))
# values.sort()
# i_n = ((N-1)//2)
# print("{}".format(values[i_n]))

# #2068

# T = int(input())

# for i in range(T):
#     numbers = list(map(int, input().split()))
#     print(f'#{i+1} {max(numbers)}')


# T = int(input())
# for i in range(T):
#     l = list(map(int, input().split()))
#     l_max = 0
#     for j in l:
#         if l_max < j:
#             l_max = j
#     print('#%d %d' %((i+1), l_max))


# #2072.

# T = int(input())
# for i in range(T) :
#     numbers = list(map(int, input().split()))
#     odd_sum = 0
#     for j in numbers :
#         if (j % 2 != 0) :
#             odd_sum += j

#     print ("#%d %d" %((i+1), odd_sum))

