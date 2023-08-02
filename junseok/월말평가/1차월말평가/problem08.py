############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calculate_sum_number(word):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    str_sum = 0 #합을 더할 str_num 변수 초기값 0설정
    list_word = list(map(str,word)) #word 인자의 리스트를 분리해서 list_word의저장
    for i in list_word: #list_word 의 i요소를 순회
        if i.isdigit() == True: #만약 i요소가 숫자라면
            str_sum += int(i) #str_num변수에 i 더하기
    return str_sum #str_sum  반환
 




# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(calculate_sum_number('ab123cd45ef6')) # => 21
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    