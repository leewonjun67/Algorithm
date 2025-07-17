def solution(s):
    answer = ''
    n = len(s)

    if (n % 2 == 1) and (n > 0):
        answer = s[n // 2]
    else :
        answer = s[n // 2 - 1 : n // 2 + 1]
    return answer


# 논리연산자를 이용하여 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
# s = abcde , c
# s = qwer , we