def is_user_data_valid(user_data):
    if user_data.get('id') == '':   # id값이 빈 값이면 false
        return False
    elif user_data.get('password') == '':   # password값이 빈 값이면 false
        return False
    else:   # id, password 값이 둘다 빈값이 아닐경우 true
        return True

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