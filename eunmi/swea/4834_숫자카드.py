# 케이스 개수 정수로 받기
T = int(input())

# test case 반복 횟수
# 빈 리스트를 만들어서
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    c = [0] * (max(arr)+1)
    max_v = 0

# 각각의 숫자 인덱스 카운트 = 같은 숫자의 카드 장수
# for문 range = arr 길이만큼
    for i in range(N):
        c[arr[i]] += 1
# 현재의 max_v VS c의 인덱스에 가장 큰 숫자 -> 가장 많은 장수의 카드 찾기
        max_v = max(max_v, c[arr[i]])
# 인덱스에 해당하는 숫자 찾기위한 세팅
    res_idx = 0
# 같은 장수의 카드가 있을 경우, 큰 숫자가 출력
# 9-0 순서대로 뒤에서부터 찾기 (n-1부터 인덱스가 -1이 되면 종료, -1만큼 빼면서 비교)
    for i in range(len(c)-1, -1, -1):
        # print(i, c[i])
        if c[i] == max_v:

            res_idx = i
            break

    print(f'#{tc} {res_idx} {max_v}')