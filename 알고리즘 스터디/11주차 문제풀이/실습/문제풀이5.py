# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    return len(stack) == 0
    
s = "()()"
print(solution(s))