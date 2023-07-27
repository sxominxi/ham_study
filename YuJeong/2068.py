# 최대수 구하기

import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(1, t+1):
    nums = list(map(int,input().split()))
    
    max_num = nums[0]
    for j in nums:
        if max_num < j:
            j = max_num
        else:
            continue
    print(f'#{i} {j}')