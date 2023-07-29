# 정싸피는 이번 프로젝트에서 회원가입 유효성 검사팀에 들어가게 되었다.
# 유효성 검사팀은 회원가입 과정에서 유저가 입력한 정보를 검사하는 프로그램을 만드는 팀
# 이다.
# 팀 회의를 통해 정싸피가 맡아서 개발해야하는 기능들이 정해졌다고 할 때, 아래의 문제들
# 을 해결하여 정싸피를 도와주도록 하자.

# 신규 생성 아이디의 마지막 글자는 반드시 0부터 9 사이의 숫자로 끝나야한다.
# 사용자의 입력 정보인 user_data가 python의 dictionary 형태로 들어온다고 할 때,
# 사용자가 입력한 아이디가 위 조건을 만족하면 True, 그렇지 않으면 False를 반환하는
# is_id_valid 함수를 완성하시오.

def is_id_valid(user_data):
    if user_data.get('id')[-1] == '1': # user_data.get('id')[-1]의 type이 str 이라서 ' ' 안에 넣어줘야함
        return True
    elif user_data.get('id')[-1] == '2':
        return True
    elif user_data.get('id')[-1] == '3':
        return True
    elif user_data.get('id')[-1] == '4':
        return True
    elif user_data.get('id')[-1] == '5':
        return True
    elif user_data.get('id')[-1] == '6':
        return True
    elif user_data.get('id')[-1] == '7':
        return True
    elif user_data.get('id')[-1] == '8':
        return True
    elif user_data.get('id')[-1] == '9': # 이거 어캐 줄이냐 ㅋㅎㅋㅎ
        return True
    else:
        return False

# type((user_data.get('id')[-1])) 하려고 봤더니 문자열이네 ㅎ ㅎ
if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
    # 아래 부터 추가 예제 코드 작성 가능합니다.