# https://school.programmers.co.kr/learn/courses/30/lessons/181882

def solution(arr):
    answer = []
    a = len(arr)
    for i in range(a):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            answer.append(arr[i] // 2)
        elif arr[i] >= 50 and arr[i] % 2 != 0:
            answer.append(arr[i])
        elif arr[i] < 50 and arr[i] % 2 == 1:
            answer.append(arr[i] * 2)
        else:
            answer.append(arr[i])
        
    return answer

arr = [1,2,3,100,99,98]
print(solution(arr))