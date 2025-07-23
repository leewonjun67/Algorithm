n = int(input('수를 입력해주세요: '))
answer = []

for i in range(1, n+1):  
    if i % 2 == 1:       
        answer.append(i)

print(f'{answer}입니다')

#정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
    