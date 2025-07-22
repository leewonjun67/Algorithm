n = int(input('수를 입력해주세요: '))
answer = []

for i in range(1, n+1):  
    if i % 2 == 1:       
        answer.append(i)

print(f'{answer}입니다')

    