############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def count_over_speed(speed_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    cnt = 0 #카운트 변수 0으로 초기값 설정
    for i in speed_list:  #리스트형태의 imput을 순회
        if i > 100: #i번째 요소가 100km를 넘을 경우
            cnt += 1 #cnt변수에 +1
    return cnt #for문이 완료된 후 cnt 변수 리턴
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(count_over_speed([119, 124, 178, 192,]))  #=> 4

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    print(count_over_speed([119, 124, 178, 192, 101, 90, 50, 60, 200]))  #추가 테스트
    
