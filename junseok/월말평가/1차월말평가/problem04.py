############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def make_answer(security_str, security_code):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    char = '' #빈 문자열 char 변수 설정
    all_code = list(map(str,security_str)) #all_code 변수에 security_str 값 리스트로 변환해서 할당
    for i in security_code: #security_code 리스트 안에 있는 요소들을 순회하며
        char += all_code[i] #security_code 리스트 안에 있는 i요소를 all_code 에서 뽑아서 char 문자열에 더하기
    return char #char 리턴
        
    
    

# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    answer = make_answer('kXeFSOo1spkSMsuuoAiklFeqYz', [4,11,17,21,24])
    print(answer)   # => SSAFY
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    