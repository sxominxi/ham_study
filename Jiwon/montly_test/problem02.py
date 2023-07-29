def under_60(scores):
    # 여기에 코드를 작성합니다.
    '''
    60점 미만인 
    과목의 개수를
    계산하는 함수
    '''
    num = 0                # 카운트 할 변수 선언, 초기값이므로 0
    for i in scores:       # 반복문으로 원소 하나씩 60안넘는지 확인
        if i < 60:         # 60 안넘는지 확인
            num += 1       # 안넘으면 +1
    return num             # num을 return


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.

