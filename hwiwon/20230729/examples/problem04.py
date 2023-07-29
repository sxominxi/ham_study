def is_id_valid(user_data):
    user_id = user_data.get('id')
    id_s = []
    for i in user_id:
        id_s.append(i)
    try:    
        int(id_s[-1])
        return True
    except:
        return False 

    # 여기에 코드를 작성합니다.
##입력 str 개별적으로 리스트에 추가
##입력된 마지막 값을 int 로 지정할 수 있다면 True, 에러가 난다면 False

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
