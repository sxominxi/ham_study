# 정싸피는 이번 프로젝트에서 회원가입 유효성 검사팀에 들어가게 되었다.
# 유효성 검사팀은 회원가입 과정에서 유저가 입력한 정보를 검사하는 프로그램을 만드는 팀
# 이다.
# 팀 회의를 통해 정싸피가 맡아서 개발해야하는 기능들이 정해졌다고 할 때, 아래의 문제들
# 을 해결하여 정싸피를 도와주도록 하자.

# 신규 아이디 생성 시 아이디와 비밀번호 모두 빈 값이 입력되는 것을 방지하고자 한
# 다.
# 사용자의 입력 정보인 user_data가 python의 dictionary 형태로 들어온다고 할 때, 사
# 용자가 입력한 아이디와 비밀번호 중 하나라도 “비어있는 문자열”이면 False, 그렇지
# 않으면 True를 반환하는 is_user_data_valid 함수를 완성하시오.

def is_user_data_valid(user_data):
    if user_data.get('id') == '': # id의 value가 ''이면 False 반환하기
        return False
    elif user_data.get('password') == '':
        return False
    else:
        return True
    
# len(user_data.values())를 사용하려고 했는데 둘 다 개수가 2네

# 의문 : 어쨋든 답은 맞게 나오는데 입력을 안한 상태, None 일 때 이렇게 하는게 맞나 ?

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True
    # 아래 부터 추가 예제 코드 작성 가능합니다.

# try except 를 쓰는 문제가 아닌가 음 음 음
