import random

lotto = random.sample(range(1, 46), 6)


while True:
    
    my = input("로또 번호 6개를 입력하세요 (띄어쓰기로 구분): ")
    my_numbers = list(map(int, my.split()))

    if len(my_numbers) != 6:
        print("숫자 6개를 입력해야 해요!")
        continue

    if not all(1 <= n <= 45 for n in my_numbers):
        print("모든 숫자는 1부터 45 사이여야 해요!")
        continue

    if sorted(my_numbers) == sorted(lotto):
        print(" 축하합니다! 로또에 당첨됐어요!")
        break
    else:
        print("아쉽네요! 다시 도전해보세요 ")
