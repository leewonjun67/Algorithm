# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    arr = arr[:]  
    i = 0
    while i < len(arr):
        if arr[i] == arr[i]:
            arr.pop(i)
            
        else:
            i += 1
    return arr

arr = [1,1,3,3,0,1,1]
print(solution(arr))