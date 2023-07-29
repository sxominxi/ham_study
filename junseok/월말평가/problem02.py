def under_60(scores):
    cnt = 0 #cnt변수에 초기값0 참조
    for score in scores: #scores 리스트를 순회하며
        if score < 60: #만약 score가 60미만 일때
            cnt += 1 #cnt 변수에 1더하기
    return cnt #for문 전부 순회후 cnt 변수 리턴
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.

