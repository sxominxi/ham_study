def is_id_valid(user_data):
    id_data = {}    # 빈 dict 생성
    id_data.update(user_data)   # user_date 담기
    value = list(id_data.values())  # value 값만 받아서 list만들기
    
    try:
        int(value[0][-1])   # [0]은 id의 value, id value에서 마지막이 int로 변환
        return True # 가능하면 true
    except:
        return False    # 불가능하면 false
    
# 근데 이거 try-except말고 if-else로 하면 왜 오류가 뜰까요..


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
