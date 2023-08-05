
T = int(input())

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        minIdx = i
        for j in range(i + 1, n):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr


for tc in range(1, T+1):
# sort 쓰지말고 정렬하기 -> 선택정렬, 버블정렬 (오름차순)
# 오름차순으로 출력

    N = int(input())
    arr = list(map(int, input().split()))
    arr = selectionSort(arr)
    # print(arr)
    # 새로 정렬하는 것을 받을 빈 리스트 생성
    num_list = []

    # 10개까지만 출력
    for i in range(5):
    # i하나당 큰거하나 작은거하나 총 2개 출력
    # num 리스트에 append
        num_list.append(arr[len(arr)-1-i])
        num_list.append(arr[i])

    # list -> str 형식으로 바꿔서 출력
    result = ''
    for i in range(len(num_list)):
        result += str(num_list[i]) + " "

    print(f'#{tc} {result}')