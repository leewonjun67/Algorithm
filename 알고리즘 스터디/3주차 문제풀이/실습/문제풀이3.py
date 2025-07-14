#구구단 응용버전 
start = int(input("시작 단 입력: "))
end = int(input("끝 단 입력: "))
a = input("전체, 짝수, 홀수 셋 중에 뭐 출력할래? ")

for k in range(start, end + 1):
    if a == "짝수" and k % 2 != 0:
        continue
    elif a == "홀수" and k % 2 == 0:
        continue

    print(f"--- {k}단 ---")
    for i in range(2, 10):
        print(f"{k} x {i} = {k * i}")
    print()

# 시작단을 2, 끝 단을: 6 , a = 짝수로함 출력은 2단,4단,6단 출력됨