def is_id_valid(user_data):
    # 여기에 코드를 작성합니다.
    pass_code =['0','1''2','3','4','5','6','7','8','9'] # pass가 가능한 코드는 0~9까지
    if user_data['id'][-1] in pass_code: # user_data id의 밸류값의 마지막 인덱스가 pass code 안에 있으면 참
        return True
    else:
        return False # 이외의 모든 값은 거짓

    

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
