# https://school.programmers.co.kr/learn/courses/30/lessons/120880?utm_source=chatgpt.com
def solution(numlist, n):
    
    for i in range(len(numlist)-1):
        for j in range(len(numlist)-i-1):
            if numlist[j] >= n:
                num1 = numlist[j] - n
            else:  
                num1 = n - numlist[j] 

            if numlist[j+1] >= n:
                num2 = numlist[j+1] - n
            else:
                num2 = n - numlist[j+1]  
            
            if num1 > num2:
                numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
            elif num1 == num2 and numlist[j] < numlist[j+1]:
                numlist[j], numlist[j+1] = numlist[j+1], numlist[j]
    
    return numlist

numlist = [1,2,3,4,5,6]
n = 4
print(solution(numlist,n))