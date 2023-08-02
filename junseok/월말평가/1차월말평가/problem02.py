############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_average(speed_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    over_car_sum = 0 #위반차량합 변수에 초기값 0 설정
    cnt = 0 #카운트 변수 0으로 초기값 설정
    for i in speed_list:  #리스트형태의 imput을 순회
        if i > 100: #i번째 요소가 100km를 넘을 경우
            cnt += 1 #cnt변수에 +1
            over_car_sum += i #over_car_sum 에 위반 속도 더하기
    mean_speed = over_car_sum / cnt #위반차량 속도합에 위반차량 수 나누기
    return mean_speed #평균속도 리턴
    
    
    
    
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calc_average([119, 124, 178, 192,]))  #=> 153.25
    
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    print(calc_average([119, 124, 178, 192, 101, 90, 50, 60, 200]))  #추가 테스트 => 152.333333..
    