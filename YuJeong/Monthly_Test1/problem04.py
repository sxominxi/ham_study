# 1번 방법

def is_id_valid(user_data):
    data = {}
    data.update(user_data)
    value = list(data.values()) # 딕셔너리의 value값만 뽑아서 리스트 안에 넣음
    
    try:
        int(value[0][-1])  # id 마지막 값을 정수로 변환 가능한 경우 True
        return True
    except:     # 오류가 뜨는 경우 False 출력
        return False
    


# 2번 방법
# try - except 구문을 OOP 시간에 배워서 다른 방법으로 풀었습니다.    
def is_id_valid(user_data):
    data = {}
    data.update(user_data)
    value = list(data.values())  # 딕셔너리의 value값만 뽑아서 리스트 안에 넣음
    
    if value[0][-1] in list(map(str,range(10))):  # id의 마지막 값이 문자열이기 때문에 문자열 0~9안에 있는지 확인
        return True
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
