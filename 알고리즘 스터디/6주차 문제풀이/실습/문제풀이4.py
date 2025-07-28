# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1,s2,s3 = 0,0,0
    
    for i, n in enumerate(answers):
        if n == supo1[i%5]:
            s1 += 1
        if n == supo2[i%8]:
            s2 += 1
        if n == supo3[i%10]:
            s3 += 1
    
    score = [s1,s2,s3]   
    
    for i, n in enumerate(score):
        if n == max(score):
            answer.append(i+1)
       
      
    return answer
answers = [1,2,3,4,5]
print(solution(answers))