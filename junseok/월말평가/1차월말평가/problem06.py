############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def caesar(word, num):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    list_word = list(map(str,word)) #word 인자에 들어간 문자열 list로 변환
    char = '' #빈 문자열 char 변수 생성
    for i in list_word:  #list_word 를 순회하면서
        if  96 < ord(i)< 122: #i요소의 ord값 확인(소문자의경우)
            char_num = ord(i) + num%26 #num을 알파벳의 갯수인 26으로 나눈 값을 ord(i) 더함
            if char_num > 122: #만약 더한값이 ord('z')값보다 크면 -26
                char_num -= 26 
        elif  64 < ord(i)< 91: #i요소의 ord값 확인(대문자의경우)
            char_num = ord(i) + num%26  #num을 알파벳의 갯수인 26으로 나눈 값을 ord(i) 더함
            if char_num > 122: #만약 더한값이 ord('Z')값보다 크면 -26
                char_num -= 26
        char += chr(char_num) #char 변수에 반환된 값 더하기
    return char #리턴 char

            
        
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    print(caesar('ssafy', 1))   # => ttbgz
    print(caesar('Python', 10)) # => Zidryx
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    