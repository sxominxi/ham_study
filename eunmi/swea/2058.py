# 1
number = list(input())
number = list(map(int, number))
sum_list = sum(number)
print(sum_list)

# 2
data = input()
answer = 0

for num in data:
	answer = answer + int(num)
print(answer)