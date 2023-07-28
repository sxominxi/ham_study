def is_user_data_valid(user_data):
    if user_data.get('id') == '': #주어진 딕셔너리 값중 키가 id인 값이 빈 문자열이라면
        return False #False를 리턴
    elif user_data.get('password') == '': #주어진 딕셔너리 값중 키가 password인 값이 빈 문자열이라면
        return False #False를 리턴
    else: #나머지의 경우 모두 True를 리턴
        return True
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
    # True
    # 아래 부터 추가 예제 코드 작성 가능합니다.
