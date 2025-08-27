# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = []
    
    while arr:
        a = arr.pop()
        if len(answer) == 0:
            answer.append(a)
        else:
            if answer[-1] != a:
                answer.append(a)
    return answer[::-1]

arr = [1,1,3,3,0,1,1]
print(solution(arr))