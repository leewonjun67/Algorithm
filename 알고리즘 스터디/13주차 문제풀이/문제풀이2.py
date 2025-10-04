#https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))

[("u","sun"), ("e","bed"), ("a","car")]
