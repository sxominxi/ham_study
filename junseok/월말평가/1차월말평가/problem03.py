############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def calc_item_price(item_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_price = 0 #전체 가격을 나타내는 sum_price 초기값 0 설정
    for i in range(len(item_list)): #for문으로 item_list의 딕셔너리 갯수만큼 반복
        count = item_list[i]['count'] #i번째 item_list의 count값 할당
        price = item_list[i]['price'] #i번째 item_list의 price값 할당
        sum_price += count * price #sum_price의 두개의 변수값을 곱한 값 더하기
    return sum_price #sum_price 리턴
   
   
    
# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    SSAFANG_ITEM_LIST = [
        {
          'name': 'Galaxi Buds',
          'count': 3,
          'price': 150000,
        },
        {
          'name': 'Galaxi Pro Book 3',
          'count': 2,
          'price': 1500000,
        },
        {
          'name': 'Galaxi Mouse Pro',
          'count': 3,
          'price': 21000,
        },
    ]
    print(calc_item_price(SSAFANG_ITEM_LIST))  # => 3513000
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    