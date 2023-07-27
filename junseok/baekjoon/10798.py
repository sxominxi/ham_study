matrix = ['']*5
max_len = 0

for i in range(5):
    matrix[i] = list(map(str,input())) #입력값 리스트로 변경
    if len(matrix[i]) >= max_len:
        max_len = len(matrix[i]) #max_len에 가장 긴 리스트 참조

for i in range(max_len): #가장 긴 행만큼 반복
    for j in range(5): #열의 횟수 만큼 반복
        try: #값이 있으면 출력
            print(matrix[j][i], end='')
        except: #없으면 pass
            pass
        #1