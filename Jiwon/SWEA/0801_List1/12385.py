import sys
sys.stdin = open('input_12385.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    chas = list(map(int, input().split()))

    lo = 0                            # 현재 위치 초기화
    cnt = []                          # 충전 횟수를 셀 카운트
    while lo + K <= N:                # 현재 위치 + 최대 거리가 정류장 번호보다 작거나 같을 때 반복
        for i in range(M-1):          # 충전기
            if chas[i+1] - chas[i] > K:
                print(0)
                break
            elif lo + K >= chas[i]:   # 카운트 넣어야하는데..
                new_lo = chas[i]
            else:
                continue
            lo = new_lo
            cnt.append(new_lo)
    print(len(cnt))