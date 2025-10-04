# 순수한 재귀 함수 구현하기

def recur(n: int) -> int:
    "순수한 재귀 함수 recur의 구현"

    if n >0:
        recur(n - 1) # 왼쪽재귀
        print(n)     # 현재  n출력
        recur(n - 2) # 오른쪽재귀

x = int(input('정수값을 입력해주세요: '))

recur(x)