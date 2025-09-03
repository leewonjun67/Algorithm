# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    answer = []
    
    Emergency = sorted(emergency, reverse = True)
    
    for i in emergency:
        answer.append(Emergency.index(i) + 1)            #index= Emergency에서 몇번쨰에 있는지
           
    return answer



emergency = [3,76,24]
print(solution(emergency))