def is_user_data_valid(user_data):
    # 여기에 코드를 작성합니다.
        if '' == user_data['id'] or '' == user_data['password']:    # 왜 여기서 in을 쓰면 안되고 ==를 쓰면 되는걸까
            return False                                            # ''(공백)이 user_data 딕셔너리의 value에 있냐
        else:
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
