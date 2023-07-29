# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    # 여기에 코드를 작성합니다.
    min = scores[0]           # 최솟값 저장 할 min 만들기, 초기값은 비교를 위한 scores[0]
    for i in scores:          # scores 반복문을 돌리며
        if i <= min:          # i와 min(최솟값)을 비교
            min = i           # i가 더 작다면 min에 할당
    return min                # min_score는 min값을 return



if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    
