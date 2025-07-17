#1부터 n까지 중에서 3의 배수이면서 홀수인 수의 합을 구하기
#1-3을 응용해서 풀 수 있음.
#n의 값을 입력하는 필드 작성 필수

n = int(input('숫자를 입력해주세요: '))

sum = 0
for i in range(1, n+1):
    if i%3 == 0 and i%2 == 1:
        sum += i
    
print(sum)
    

