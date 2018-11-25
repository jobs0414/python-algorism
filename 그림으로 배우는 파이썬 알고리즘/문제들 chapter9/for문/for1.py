s = "I have a dream"

letter = input("찾고자 하는 문자를 입력해주세요")

found = False

for f in s: 
    if f == letter: 
        found = True
        break; 

if found==True: 
    print("찾았다",letter)


else: 
    print(letter,"를못찾았다 ㅠ ")