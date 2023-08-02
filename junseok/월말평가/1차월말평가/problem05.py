############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def change_pwd(word, secret_code):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    list_word = list(map(str,word)) #input문자열word를 리스트 형태로 변환
    char = '' #빈 문자열 변수 char 설정
    for i in list_word: #list_word 를 순회하며
        char += str(secret_code.get(i)) #딕셔너리 표에 있는 값중 list_word 값과 동일한 요소 get 후에 str 타입으로 바꾼후 char에 더하기
    return char #최종 char 리턴


    
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    secret_code = {
        'a': 3,    'b': 8,    'c': 0,    'd': 1,
        'e': 7,    'f': 6,    'g': 7,    'h': 1,
        'i': 2,    'j': 5,    'k': 3,    'l': 6,
        'm': 5,    'n': 0,    'o': 7,    'p': 9,
        'q': 8,    'r': 2,    's': 4,    't': 9,
        'u': 6,    'v': 3,    'w': 2,    'x': 4,
        'y': 8,    'z': 1,    ' ': 0,
    }
    print(change_pwd('ssafy', secret_code)) # => 44368
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    print(change_pwd(' ssafy ', secret_code)) # => 0443680 추가케이스
    