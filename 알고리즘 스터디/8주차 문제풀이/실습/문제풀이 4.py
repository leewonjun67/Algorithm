# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums): 
    choose = []
    limit = len(nums) // 2
    
    for i in nums:
        if i not in choose:
            choose.append(i)
        if len(choose) == limit:
            break
            
    return len(choose)

nums = [3,1,2,3]
print(solution(nums))