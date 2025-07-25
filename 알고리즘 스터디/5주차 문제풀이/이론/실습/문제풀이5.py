# https://school.programmers.co.kr/learn/courses/30/lessons/181918

def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    
    return stk
arr = [1,4,2,5,3]
print(solution(arr))
