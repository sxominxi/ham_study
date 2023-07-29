char = input()
new_char = char.upper()

list1 = [0] * len(char)
cnt = 0

for i in new_char:
    if i in new_char:
        list1[cnt] += 1
    cnt += 1

print(list1)