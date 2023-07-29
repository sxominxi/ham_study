def is_user_data_valid(user_data):
    data = {}
    data.update(user_data)  # 빈 리스트에 딕셔너리 추가
    if '' in data.values() or '' in data.keys():
        # 공백있는 문자열이 딕셔너리 값에 있을 경우
        return False
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
    user_data3 = {
        'id': 'jungssafy',
        ' ': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data3))