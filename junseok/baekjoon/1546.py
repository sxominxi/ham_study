N = int(input())

score = list(map(int,input().split()))

sum_score = 0
for i in score:
    sum_score += i/max(score) * 100

print(sum_score / N)
    
