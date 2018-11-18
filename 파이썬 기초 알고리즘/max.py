print("몸무게 가장 많이 나가는 사람 찾아보자")
a = int(input("입력"))
b = int(input("입력"))
c = int(input("입력")) 

max_weight = a 

if max_weight < b: 
    max_weight = b

if max_weight < c: 
    max_weight =c 


print(max_weight)