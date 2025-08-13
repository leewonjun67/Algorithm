# https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = [0]  
    for num in numbers:
        my = []
        for i in answer:
            my.append(i + num)
            my.append(i - num)
        answer = my
    return answer.count(target)

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))
