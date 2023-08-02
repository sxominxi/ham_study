############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, min, max, len 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def get_row_col_maxsum(matrix):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    cnt_c = 0
    for _ in matrix:
        cnt_c +=1
    cnt_r = 0
    for _ in matrix[0]:
        cnt_r += 1
    
    sum_list_r = []
    for i in range(cnt_c):
        sum_r = 0
        for j in range(cnt_r):
            sum_r += matrix[i][j]
        sum_list_r.append(sum_r)
    
    sum_list_c = []
    for i in range(cnt_r):
        sum_c = 0
        for j in range(cnt_c):
            sum_c += matrix[j][i]
        sum_list_c.append(sum_c)
        
    max_r = sum_list_r[0]
    for i in sum_list_r:
        if max_r < i:
            max_r = i

    max_c = sum_list_c[0]
    for i in sum_list_c:
        if max_c < i:
            max_c = i        


    if max_r < max_c:
        return ('col', max_c)
    else:
        return ('row', max_r)
    

            
    


# 아래 코드는 실행 확인을 위한 코드입니다.
if __name__ == '__main__':
    # 예시 코드는 수정하지 마세요.
    example_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    example_matrix2 = [
        [11, 5, 49, 20],
        [28, 16, 20, 33],
        [63, 17, 1, 15]
    ]
    print(get_row_col_maxsum(example_matrix))   # => ('row', 58)
    print(get_row_col_maxsum(example_matrix2))  # => ('col', 102)

    # 여기부터 아래에 추가 테스트를 위한 코드 작성 가능합니다.
    