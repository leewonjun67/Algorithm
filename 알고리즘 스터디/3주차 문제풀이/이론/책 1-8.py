print('1부터 n까지 정수의 합을 구하시오')
n = int(input('n값을 입력해주세요:'))

sum = 0

for i in range(1,1+n):
    sum += i

print(f'1부터 {n}까지 정수의 합은{sum}입니다')
print(f'i값은 {i}입니다')