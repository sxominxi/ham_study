# 1
def under_60(scores):
    nums = []   # 빈 list만들기
    for i in scores:
        if 60 > i:
            nums.append(i) # 60점 미만 점수들만 빈리스트에 담기
    return len(nums) 
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.

# 2
def under_60(scores):
    i = 0   
    count = 0   # 초기값 0
    if 60 > scores[i]:
        i += 1  # 인덱스 하나씩 올리면서 찾기
        count += 1
        return count
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.