print('저장된 비밀번호가 아니면 비밀번호가 맞을때까지 반복하는 코드')

while True:
    password = (input('비밀번호 입력: '))
    if password == 'good':
        print('접속성공')
        break
    else: 
        print('비밀번호가 틀렸습니다 다시 입력해주새요:')
       