# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
   
        count = 0
        if progresses[0] >= 100:  
            for _ in range(len(progresses)):
                if progresses[0] >= 100:
                    count += 1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    break

        if count > 0:
            answer.append(count)

    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))
