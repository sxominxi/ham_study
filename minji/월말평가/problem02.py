# 전체 점수 중 60점 미만인 과목의 개수를 계산하는 함수 under_60을 완성하시오.

def under_60(scores):
    subject = 0 # 값 초기화
    if scores[0] < 60:
        subject += 1
    elif scores[1] < 60:
        subject += 1
    elif scores[2] < 60:
        subject += 1
    elif scores[3] < 60:
        subject += 1
    return subject
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.

# 다 if로 작성하면 어캐 되려나
