paper_num = int(input())
rect =[[0]*100 for i in range(100)]
for i in range(paper_num):   
    x,y= map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            if rect[i][j] ==0:
                rect[i][j]= 1
            else:
                continue
sum =0
for num in rect:
 sum += num.count(1)

print(sum)