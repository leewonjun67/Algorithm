# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    nx = list(map(int, str(n)))
    a = len(nx)
    for i in range(a // 2):
       nx[i], nx[a-i-1] = nx[a-i-1], nx[i]
    
    return  nx

n=12345
print(solution(n))