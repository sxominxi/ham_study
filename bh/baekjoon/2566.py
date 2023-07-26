arr =[]
for i in range(9):
    arr_num =list(map(int,input().split()))
    arr.append(arr_num)
max= 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max: # 등호의 여부에 따라 달라짐.
            max =arr[i][j]
            x = i+1
            y = j+1
if x ==0 and y ==0:
    x = 1
    y = 1

print(max)
print(x,y)

