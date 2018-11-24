count_a =0 
count_b=0
count_c =0 

for i in range(5): 
    a=int(input("숫자입력 "))


    if a <=9: 
        count_a +=1

    elif a >=10 and a<101: 
        count_b +=1

    elif a >100 and a<1001:
        count_c +=1 



print(count_a,count_b,count_c) 