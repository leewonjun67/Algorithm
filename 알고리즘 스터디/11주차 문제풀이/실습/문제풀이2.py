# https://school.programmers.co.kr/learn/courses/30/lessons/181851

def solution(rank, attendance):
    answer = 0
    
    ra = []
    
    for i in range(len(rank)):
        if attendance[i]:
            ra.append((i,rank[i]))
            
    ra.sort()
    for i in range(len(ra)):
        for k in range(i+1, len(ra)):
            if ra[i][1] > ra[k][1]:
                ra[i],ra[k] = ra[k],ra[i]
                
    a,b,c = ra[0][0], ra[1][0], ra[2][0]
    
    return 10000 * a + 100 * b + c
    
    
rank = [3,7,2,5,4,6,1]
attendance = [False, True, True, True, True, False, False]
print(solution(rank,attendance))