# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    score = scores[0]  # list 첫 번째 값
    for i in scores:
        if score > i:  
        # list 안에 있는 값 하나씩 뽑아서 첫 번째 값이랑 비교
        # 더 낮으면 i로 대체
            score = i
    return score


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.