def under_60(scores):
    count = 0 # 60보다 작은 값을 세는 변수
    for i in scores: # 점수가 들어있는 리스트를 순회
        if i<60: # 값이 60보다 작을 경우
            count +=1 # count에 +1
    return count # 개수를 센 변수를 반환
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    scores = [30,40,50,60,70,80] # 3(추가 예제코드 작성)
    print(under_60(scores))
