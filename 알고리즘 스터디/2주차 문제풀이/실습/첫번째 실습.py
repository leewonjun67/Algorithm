score = int(input())

if 90 <= score <=100: 
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

#점수가 90이상 100이하이면 a 출력
#점수가 80 이상 89이하이면 b출력
#점수가 70 이상 79이하이면 c출력
#점수가 60 이상 69이하이면 d 출력
#위에 조건문에 해당되지 않는 숫자 나오면 f출력