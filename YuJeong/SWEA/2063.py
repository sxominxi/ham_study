# 중간값 찾기

import sys
sys.stdin = open('input2.txt')

N = int(input())
nums = list(map(int,input().split()))

nums.sort()
print(nums[N//2])