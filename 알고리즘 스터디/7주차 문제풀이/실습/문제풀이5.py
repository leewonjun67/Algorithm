# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    
    
    # a는 answer길이
    # j는 answer 인덱스 만큼 반복문 돌림
    # k는 answer 길이 만큼 반복문 돌림
    
    for i in strings:
        answer.append((i[n], i))
        
    a = len(answer)
    for j in range(len(answer)):
        for k in range(0, a-j-1):
            if answer[k][0] > answer[k+1][0]:
                answer[k],answer[k+1] = answer[k+1],answer[k]
            
            elif answer[k][0] == answer[k+1][0] and answer[k][1] > answer[k+1][1]:
                answer[k],answer[k+1] = answer[k+1],answer[k]
    
    return [x[1] for x in answer]
                               
                
            
strings = ["sun", "bed", "car"]
n =1
print(solution(strings, n))

