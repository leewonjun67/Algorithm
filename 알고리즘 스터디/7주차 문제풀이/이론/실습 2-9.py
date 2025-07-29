# 1000 이하의 소수를 나열하기(실습2-8 개선)

counter = 0                  # 나눗셈 횟수 카운트
ptr = 0                      # 이미 찾은 소수의 개수 즉 prime 배열 안에 들어가있는 원소 개수
prime = [None] *500          # 소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

for n in range(3,1001,2):   # 홀수만 나오게 차피 짝수는 2제외하고 소수안됨 
    for i in range(1, ptr):
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr]= n
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈한 총 횟수: {counter}')
