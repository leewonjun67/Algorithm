# https://school.programmers.co.kr/learn/courses/30/lessons/181854

def solution(arr, n):
    result = []
    if len(arr) % 2 == 1: 
        for i in range(len(arr)):
            if i % 2 == 0:
                result.append(arr[i] + n)
            else:
                result.append(arr[i])
    else: 
        for i in range(len(arr)):
            if i % 2 == 1:
                result.append(arr[i] + n)
            else:
                result.append(arr[i])
    return result
n = 27
arr =[49,12,100,276,33]

print(solution(arr,n))