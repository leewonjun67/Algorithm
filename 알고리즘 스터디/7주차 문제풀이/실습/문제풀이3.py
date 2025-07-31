# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    answer = 0
    
    wallet = sorted(wallet)
    bill = sorted(bill)
    
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        if bill[0] > bill[1] :
            bill[0] = bill[0] // 2
            
        else :
            bill[1] = bill[1] // 2
        answer += 1
        bill = sorted(bill)         
    return answer 

wallet = [30,15]
bill = [26,17]

print(solution(wallet, bill))

