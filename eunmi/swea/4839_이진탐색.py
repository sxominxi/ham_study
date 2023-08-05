
# 테스트 케이스 정수로 받기
T = int(input())

for tc in range(1, T+1):
    # 전체 쪽수, 찾을쪽수a, 찾을쪽수b 정수로 받기
    P, Pa, Pb = map(int, input().split())

    # 전체 book_page 리스트
    book_page = list(range(1, P+1))

    # 중간 결과값을 담을 a_list
    a_list = []
    # Pa 값을 찾을때까지 반복
    start = 0
    end = P - 1
    while start <= end:
        middle = (start + end) // 2
        if book_page[middle] == Pa:
            a_list.append(book_page[middle])
            # Pa 찾으면 break
            break
        elif book_page[middle] > Pa:
            a_list.append(book_page[middle])
            end = middle
        else:
            a_list.append(book_page[middle])
            start = middle
        # Pa 값을 찾을때까지 반복
        continue

    # 중간 결과값을 담을 b_list
    b_list = []
    # Pb 값을 찾을때까지 반복
    start = 0
    end = P - 1
    while start <= end:
        middle = (start + end) // 2
        if book_page[middle] == Pb:
            b_list.append(book_page[middle])
            # Pb 찾으면 break
            break
        # 교재와 똑같이 middle-1, middle+1 을 했을때 오류발생
        # 미들값을 포함시켜서 end, start를 세팅해야 테스트 반례까지 고려가능
        elif book_page[middle] > Pb:
            b_list.append(book_page[middle])
            end = middle
        else:
            b_list.append(book_page[middle])
            start = middle
        # Pb 값을 찾을때까지 반복
        continue

    # a_list와 b_list 길이 비교
    # 길이가 짧은 쪽 출력
    if len(a_list) < len(b_list):
        print(f'#{tc} A')
    elif len(a_list) > len(b_list):
        print(f'#{tc} B')
    # 같을 경우 0 출력
    else:
        print(f'#{tc} 0')
