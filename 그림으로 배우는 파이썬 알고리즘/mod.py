n1= int(input("숫자를 입력하세요 1"))
n2= int(input("숫자를 입력하세요 2"))

if n1%2 ==0 and n2%2==0:
    print("모두 짝수")

elif n1%2==1 and n2%2==1:
    print("모두 홀수")


else: 
    print("특별하지 않네요")