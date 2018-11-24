count_a =0 
count_b =0 

for i in range(0,4): 
    a = int(input("숫자 입력"))
    b = int(input("숫자 입력"))

    if a>b: 
        count_a +=1 

    if b>a: 
        count_b +=1


print(count_a,count_b)
