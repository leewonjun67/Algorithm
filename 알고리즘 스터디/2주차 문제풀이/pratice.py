name = input("이름을 입력하세요:")
age = int(input("나이를 입력하세요:"))

if age >=20 : 
    print(f"{name}은 성인입니다")
elif 0 <age and age <20 :
    print(f"{name}은 미성년자입니다")
else :
    print("잘못입력했습니다")
   