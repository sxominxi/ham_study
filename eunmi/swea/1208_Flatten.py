# max, min 안쓰고 풀기

# 테스트횟수만큼 반복
for tc in range(1, 11):
# 덤프횟수 정수로 받기
    N = int(input())
# arr 리스트, 정수, 공백
    arr = list(map(int, input().split()))

# for문 range 덤프횟수
    for i in range(N):
# max,min = 0 기본세팅
        max_num = arr[0]
        min_num = arr[0]
        max_idx = 0
        min_idx = 0
# arr리스트에서 최대 최소를 받아서 비교하는 for문
        for i in range(100):
            
# max=0 < arr[i] 비교해서 가장 큰 값 찾기
            if max_num < arr[i]:
# max = max_arr
                max_num = arr[i]
                max_idx = i

# min=0 > arr[i] 비교해서 가장 작은 값 찾기
            if min_num > arr[i]:
# min = min_arr
                min_num = arr[i]
                min_idx = i

        max_num -= 1
        min_num += 1
        arr[max_idx] = max_num
        arr[min_idx] = min_num

# 마지막까지 돌렸을때 그 값이 최대,최소가 아닐 수도 있기 때문에 확인차 다시한번 돌려줌
    for i in range(100):
        if max_num < arr[i]:
            max_num = arr[i]
            max_idx = i
        
        if min_num > arr[i]:
            min_num = arr[i]
            min_idx = i

    print(f'#{tc} {max_num-min_num}')