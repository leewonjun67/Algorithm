#https://school.programmers.co.kr/learn/courses/30/lessons/181903

def solution(q, r, code):
    answer = ''
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    
    return answer

q = 3
r = 1
code = "qjnwezgrpirldywt"
print(solution(q,r,code))