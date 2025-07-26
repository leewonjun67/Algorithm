# https://school.programmers.co.kr/learn/courses/30/lessons/120844

def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    elif direction == "left":
        return numbers[1:] + [numbers[0]]
    
numbers = [1,2,3,4]
print(solution(numbers, direction='right'))