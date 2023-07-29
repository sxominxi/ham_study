price = int(input())
val = int(input())
# 총 금액과 구매한 물건 종류의 값을 받고,
total = 0
for i in range(1,val+1): # 물건의 종류 수만큼 for문을 돌려서 
    cost, num = map(int,input().split()) # 금액과 물건 수를 입력받고
    total += cost*num # 이를 곱하여 총 금액을 도출한다.

if total == price: # 영수증 총 금액과 계산한 총 금액이 맞으면 True
    print("Yes")   # 아니면 False
else:
    print("No") 