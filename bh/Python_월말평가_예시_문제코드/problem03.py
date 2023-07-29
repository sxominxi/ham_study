def is_user_data_valid(user_data):
    if user_data['id'] != '' and user_data['password'] != '': # 유저 데이터의 밸류 값이 공백인지 아닌지 판단
        return True # 만약 둘 다 공백이 아니라면 잘 작성된 것이므로 True
    else:
        return False # 이외에는 모두 False
    # 여기에 코드를 작성합니다.


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
    True
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    user_data2 = {
        'id': '',
        'password': '',
    }
    print(is_user_data_valid(user_data2)) 
    
    user_data2 = {
        'id': 'jung',
        'password': ''
    }
    print(is_user_data_valid(user_data2)) 