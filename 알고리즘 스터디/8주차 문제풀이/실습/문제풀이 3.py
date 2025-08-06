# https://school.programmers.co.kr/learn/courses/30/lessons/120869

# def solution(spell, dic):  
#     sp = len(spell)
    
#     for i in range(sp):
#         for r in range(sp):
#             for k in range(sp):
#                 if i != r and r != k and k!= i:
#                     spelling = spell[i] + spell[r] + spell[k]
                    
#                     for n in range(len(dic)):
#                         if spelling == dic[n]:
#                             return 1
#     return 2

def solution(spell, dic):
    spelling = set(spell)
    
    for di in dic:        
        if len(di) == len(spell) and set(di) == spelling:
            return 1
    return 2

spell =["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]
print(solution(spell,dic))