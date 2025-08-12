# https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer = []
    shit = []

    for i, num in enumerate(score):
        if i < k:
            shit.append(num)
        elif shit[-1] < num:
            shit[-1] = num

        shit = sorted(shit, reverse=True)
        answer.append(shit[-1])

    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k,score))


[150, 100, 20]
answer = [10,10,10,20]
