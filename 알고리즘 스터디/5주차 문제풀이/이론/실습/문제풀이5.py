# https://school.programmers.co.kr/learn/courses/30/lessons/181918

def solution(arr):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0:
            result.append(arr[i])
    return result
arr = [1,4,2,5,3]
print(solution(arr))
