# https://school.programmers.co.kr/learn/courses/30/lessons/176963


def solution(name, yearning, photo):
    
    smu = {n: y for n, y in zip(name, yearning)}   #zip = (이름,나이)묶어서튜플생성
    # smu = { may : 5, kein : 10, kain : 1, radi : 3}
    result = []
    
    for i in photo:
        score = []
        for k in i:
            if k in smu:
                score.append(smu[k])
            else:
                score.append(0)
        
        total = sum(score)
        result.append(total)
    
    return result

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))
