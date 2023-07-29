# 전체 점수 중 최저점을 반환하는 함수 min_score을 완성하시오.

# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    lowlist = sorted(scores, reverse=False)  # scores 리스트 오름차순으로 정렬
    return lowlist[0] # 제일 작은값 출력
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.

# 의문 : scores.sort()로 하면 타입이 none으로 나오는 이유는 ?
    
# 리스트.sort()와 sorted(리스트)의 가장 큰 차이는
# 리스트.sort() 는 본체의 리스트를 정렬해서 변환하는 것이고,
# sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환하는 것입니다.