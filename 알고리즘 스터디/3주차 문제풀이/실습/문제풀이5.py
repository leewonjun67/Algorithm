N = int(input())

if 4<=N<=1000 and N%4 == 0:
    K = N // 4
    
print('long '*K +'int')


#long int는 4바이트 정수를 저장하는 값이다 8바이트 정수면 long long int로 출력됨 여기서 바이트값을 N으로 주었을때 어떻게 출력되는지 구하시오
#범위는 4<= N <=1000 4의 배수임 출력할때 공백있이 출력