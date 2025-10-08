#https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = list(map(str, numbers))
    
    
    for i in range(len(numbers)-1):
        for k in range(len(numbers)-i-1):
            if numbers[k] + numbers[k+1] < numbers[k+1] + numbers[k]: 
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
    
    return ''.join(numbers)

    
numbers = [6,10,2]   
print(solution(numbers))