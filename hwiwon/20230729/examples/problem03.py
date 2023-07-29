def is_user_data_valid(user_data):
    user_id = list(user_data.items())
    for i in range(2):
        if user_id[i][1] == '':
            return False
        else:
            return True

    # 여기에 코드를 작성합니다.
## items로 키와 벨류 값 모두 받아오기
## value 에 해당하는 인덱스값는 고정, i 로 키값만 변경 후 확인



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
