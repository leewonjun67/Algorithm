# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key : Any) -> int:
    "시퀀스 a에서 key와 일치하는 원소를 이진 검색"
    # pl은 맨 앞 원소의 인덱스, pr는 맨 뒤 원소의 인덱스, pc는 중앙 원소의 인덱스
    pl = 0                          # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1                 # 검색 범위 맨 끝 원소의 인덱스

    while True:                  
        pc = (pl + pr) // 2         # 중앙 원소의 인덱스
        if a[pc] == key:            # key는 내가 찾고자히는 값, a는 배열
            return pc               # 검색 성공
        elif a[pc] < key:           # key값이 중앙값보다 크므로 key값은 중앙값 오른쪽에 존재
            pl = pc + 1             # 검색 범위를 뒤쪽 절반으로 옮김
        else:                       # 그 반대인 key값이 중앙값보다 작을때 key값은 중앙값 왼쪽에 존재
            pr = pc +1              # 검색 범위를 앞쪽 절반으로 옮김
        if pl > pr:                 # pl이 pr보다 크면 배열안에 값이 존재하지 않다는 뜻
            break 
        return -1                   # 검색 실패
    
if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num                           # 원소수가 num인 배열을 생성

    print('배열 데이터를 오름차순으로 입력하세요.')

                  # 

    for i in range(1,num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break
    
    ky = int(input('검색할 값을 입력하세요: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다')
    else:
        print(f'검색값은 x[{idx}]에 있습니다')