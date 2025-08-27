# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    pr = [(i, p) for i, p in enumerate(priorities)]
    count = 0
    
    while pr:
        p = pr.pop(0)
        
        for q in pr:
            if q[1] > p[1]:
                pr.append(p)
                break
        else:
            count += 1
            if p[0] == location:
                return count
            
priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities,location))