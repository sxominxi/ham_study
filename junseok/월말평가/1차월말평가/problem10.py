############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def find_one(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    cnt_row = 0 #행 변수 초기값 설정 
    for i in matrix: #matrix 의 행요소 순회
        cnt_cal = 0 #열 변수 초기값 설정
        cnt_row += 1 #순회마다 행변수 1증가
        for find in i:  #열 순회
            cnt_cal += 1 #순회마다 열변수 1증가
            if find == 1: #순회하다가 1을 만났을때
                return (cnt_cal-1,cnt_row-1) #그때의 행, 열 요소 리턴
    
                
        
            


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    sample_matrix = [
      [0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]
    ]
    print(find_one(sample_matrix))  # => (1, 1)
    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    sample_matrix = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0],
      [1, 0, 0]
    ]
    print(find_one(sample_matrix)) 
    