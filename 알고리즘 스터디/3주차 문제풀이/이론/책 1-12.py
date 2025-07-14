# +와 -를 번갈아 츨력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print() #줄바꿈

# i가 홀수면 -를 출력, i가 짝수면 +를 출력
# for문이 반복될때마다 if문도 같이 반복 만약 n이 50000이면 if문도 똑같이 50000번 반복하기 때문에 조금 보기 안좋음