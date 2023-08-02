# char = input()
# new_char = char.upper()
# list1 = []

# for i in new_char:
#     list1.append(new_char.count(i))

# if list1.count(max(list1)) != max(list1):
#     print('?')
# else:
#     print(new_char[list1.index(max(list1))]) 시발 시간초과뜸 이렇게하면

char = input().upper() 
list1 = [0] * 26

for i in char:
    list1[ord(i) - ord('A')] += 1

if list1.count(max(list1)) > 1:
    print('?')
else:
    print(chr(list1.index(max(list1)) + ord('A')))