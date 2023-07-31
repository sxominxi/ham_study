def is_id_valid(user_data):
    numbers = list(map(str,range(10))) #0부터 9까지의 str요소를 가진 리스트를 numbers의 참조 
    id_list = list(map(str,user_data.get('id'))) #user_data 딕셔너리에 키값이 id인 value를 id_list에 참조
    if id_list[-1] in numbers: #id_list에 가장 마지막 요소가 0~9안에 있는 str값이라면
        return True #True를 리턴
    else: #나머지의 경우 모두 False를 리턴
        return False
    
    # 여기에 코드를 작성합니다.


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
    #1
