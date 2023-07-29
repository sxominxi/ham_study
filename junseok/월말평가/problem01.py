# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    min_num = scores[0] #min_num에 scores[0]값을 참조(초기값 설정)
    for score in scores: #scores 리스트요소를 순회
        if min_num >= score: #scores 요소중에 min_num보다 작은 경우 
            min_num = score #min_num에 score 참조

    return min_num #for문을 다 순회한후 리스트 내 가장 작은 값을 참조한 min_num return
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    
