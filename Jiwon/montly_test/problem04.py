def is_id_valid(user_data):
    # 여기에 코드를 작성합니다.

        for i in user_data['id']:                            # id 딕셔너리의 'ID' 키에서 반복
            num = i                                   # 맨마지막 i를 num에 넣기위해
    
        if num in map(str, list(range(10))):          # 0~9까지 있는지 확인 -> range(10) / list로 감싸서 str로 바꿔줌 (num이 str이라) 
            return True                               # ['1', '2', '3', '4' ... '9']중에 num(str)이 있냐
        else:
            return False


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
