import sys

matrix = []

for i in range(9):
    matrix.append(list(map(int, sys.stdin.readline().split())))

idx_row = 0 
idx_cal = 0

for row in range(9):
    for cal in range(9):
        if matrix[idx_row][idx_cal] <= matrix[row][cal]:
            idx_row = row
            idx_cal = cal

print(f'{matrix[idx_row][idx_cal]}\n{idx_row+1} {idx_cal+1}')