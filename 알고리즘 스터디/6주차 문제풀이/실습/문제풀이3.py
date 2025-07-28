# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr): 
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i + 1)                   # pop 함수는 리스트에서 마지막 요소 또는 특정 위치의 요소를 꺼내면서 제거하는 함수입니다.
            
        else:
            i += 1
    return arr

arr = [1,1,3,3,0,1,1]
print(solution(arr))