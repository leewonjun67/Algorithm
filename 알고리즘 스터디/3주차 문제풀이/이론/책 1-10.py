# a 부터 b까지 정수의 합 구하기 1

print('a 부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력해주세요:'))
b = int(input('정수 b를 입력해주세요:'))

if a > b:
    a,b = b,a

sum = 0
for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)

# 위에 처럼 for문 안에 조건문을 달아줘도 되지만 만약 a=1 이고 b=10000이 들어오면 13번행은 9999번 반복되고 15행은 단 1번 밖에 동작하지 않는 메모리를 많이 잡아먹는 방식임
# end = '' 을 사용하지 않으면 코드를 출력할때 줄바꿈이 되서 a= 3이면 3+ 이런식으로 출력 end = ''을 사용하면 줄바꿈 없이 이어서 출력해줌