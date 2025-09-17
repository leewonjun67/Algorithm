# https://school.programmers.co.kr/learn/courses/30/lessons/42840

from collections import deque

def solution(answers):
    p1 = deque([1, 2, 3, 4, 5])
    p2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    p3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    score = [2, 0, 0]

    for i in answers:
        if i == p1[0]:
            score[0] += 1
        p1.append(p1.popleft())

        if i == p2[0]:
            score[1] += 1
        p2.append(p2.popleft())

        if i == p3[0]:
            score[2] += 1
        p3.append(p3.popleft())

    max_score = max(score)

    answer = []
    for k in range(len(score)):
        if score[k] == max_score:
            answer.append(k + 1)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
