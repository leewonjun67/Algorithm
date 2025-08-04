# https://school.programmers.co.kr/learn/courses/30/lessons/12932

# return list(int(str(n)[::-1]))

def solution(n):
    nx = list(map(int, str(n)))
    a = len(nx)
    for i in range(a // 2):
       nx[i], nx[a-i-1] = nx[a-i-1], nx[i]
    
    return  nx

n=12345
print(solution(n))

nx =[1,2,3,4,5]