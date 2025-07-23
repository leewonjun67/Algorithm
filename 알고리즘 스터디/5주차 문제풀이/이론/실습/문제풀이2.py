# https://school.programmers.co.kr/learn/courses/30/lessons/181895

def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    
    p1 = arr[a1:b1+1]  
    p2 = arr[a2:b2+1]  
    
    return p1 + p2

arr = [1,2,3,4,5]
intervals = [[1,3], [0,4]]
print(solution(arr, intervals))