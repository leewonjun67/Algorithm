# https://school.programmers.co.kr/learn/courses/30/lessons/181901

def solution(n, k):
    answer = []
    
    for i in range(1, n+1):
        if i % k == 0:
            answer.append(i)
            
    return answer

n = 10
k = 3
print(solution(n,k))