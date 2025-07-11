A, B = map(int, input().split())

if A > B : 
    print(f'>')
elif A < B :
    print(f'<')
else:
    print(f'==')

#숫자 A, B가 있는데 조건문을 사용해서 A가 B보다 작으면 > 출력 B가 A보다 크면 < 출력 서로 같으면 == 출력
#문자열을 정수로 변환, sqlite는 input()에 숫자 10과 20이 들어오면 리스트형식으로 [10,20] 만들어줌