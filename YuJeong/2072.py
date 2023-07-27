# 홀수만 구하기

import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(1, t+1):
    nums = map(int,input().split())
    ans = 0
    for j in nums:
        if j % 2 == 1:
            ans = ans + j

    print('#',i, ans) 