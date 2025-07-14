print('양의 정수를 입력받아 입력된 정수들의 합이 100 이상이 되는 순간 프로그램은 입력을 멈추고, 그때까지 입력된 숫자의 개수와 총합을 출력합니다.')

total = 0
count = 0

while True:
    n = int(input('정수를 입력해주세요: '))

    if n <= 0:
        print("양의 정수만 입력해주세요.")
        continue

    total += n
    count += 1

    if total >= 100:
        break

print(f'입력된 숫자의 개수: {count}')
print(f'총합: {total}')
