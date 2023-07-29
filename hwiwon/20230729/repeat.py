### 2739

N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')
    i += 1

### 10950 

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(A + B)

### 8393

n = int(input())

A = 0
for i in range(1, n+1):
    A += i

print(A)

### 25304

X = int(input())
N = int(input())

price = 0
for i in range (1, N+1):
    a, b = map(int, input().split())
    price += a * b

if X == price:
    print('Yes')
else:
    print('No')

### 25314

N = int(input())

long_w = N // 4

def repeat():
    for i in range(1, long_w + 1):
        print('long', end=' ')
    return 'int'

print(repeat())

### 15552
T = int(input())

import sys

for i in range (1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

### 11021

import sys

T = int(input())

for i in range (1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {A + B}')

### 11022

T = int(input())

for i in range (1, T+1):
    A, B = map(int, input().split())
    print(f'Case #{i}: {A} + {B} = {A + B}')

### 2438

N = int(input())

for i in range(1, N + 1):
    star = '*'
    print(i * star)

### 2439

N = int(input())

for i in range(1, N + 1):
    star = '*'
    print((i * star).rjust(N))

### 10952

import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if (A == 0) and (B == 0):
        break
    else:
        print(A + B)

### 10951

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break