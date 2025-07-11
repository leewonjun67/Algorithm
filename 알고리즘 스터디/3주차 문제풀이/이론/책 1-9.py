# a 부터 ㅠ까지 정수의 합 구하기(for문)

print('a부터 b까지 정수의 합을 구합니다')
a = int(input('정수 a를 입력해주세요:'))
b = int(input('정수 b를 입력해주세요'))

if a > b:
    a, b = b, a # a 와 b를 오름차순으로 정렬

sum = 0 
for i in range(a,b+1):
    sum += i

print(F'{a}부터 {b}까지의 정수의 합은 {sum}입니다')