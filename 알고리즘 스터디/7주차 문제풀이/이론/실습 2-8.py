# 1000 이하의 소수를 나열하기

counter = 0

for n in range(2,1001):
    for i in range(2,n):
        counter += 1
        if n % i == 0:
            break       #break를 쓰면 안쪽 for문은 작동안하고 바깥쪽 n이 그다음 n+1로 바뀜 , 예시) n이 4일때 범위가 (2,3)인데 i가 2일대 n이 0으로 나누어 떨어지기 때문에 break문 발동 그래서 다음 n+1로 넘어가서 범위가 2,3이더라도 3은 작동할필요도 없고 작동안됨 이 논리로 9와 13도 소수 판별
    else:
        print(n)

print(f'총 나눈 횟수 : {counter}')
    