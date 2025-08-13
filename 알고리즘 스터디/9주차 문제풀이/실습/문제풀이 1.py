# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    number = str(num)
    k = str(k)
    
    for i in range(len(number)):
        if number[i] == k:
            return i + 1
    return -1

num = 29183
k = 1
print(solution(num, k))