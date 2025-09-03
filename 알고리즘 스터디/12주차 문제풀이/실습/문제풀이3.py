# https://school.programmers.co.kr/learn/courses/30/lessons/340212?language=python3

def solution(diffs, times, limit):
    max_diff = max(diffs)
    result = 0
    
    for l in range(1, max_diff + 1):           #ㅣ은 난이도 
        total = 0

        for i in range(len(diffs)):
            if i == 0:
                total += times[i]
            else:
                if diffs[i] <= l:
                    total += times[i]
                else:
                    total += (diffs[i] - l) * (times[i-1] + times[i]) + times[i]

        if total <= limit:
            result = l
            break

    return result

diffs = [1,5,3]
times = [2,4,7]
limit = 30
print(solution(diffs, times, limit))