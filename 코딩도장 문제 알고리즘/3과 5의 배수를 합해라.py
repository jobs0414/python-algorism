'''10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.'''


total=0

for i in range(1000):
    if i % 3 ==0  or i%5==0: 
        total = total + i 
print(total)


# 2번째 방법  list 배열을 만들어서 append 한것을 sum 한다. 

list=[] 

for i in range(1,1000): 
    if i %3 ==0 or i% 5==0: 
        list.append(i)

print(sum(list))

# 3번쨰 방법 한 라인으로 작성하기 

print(sum(x for x in range(1,1000) if x %3 ==0 or x % 5 ==0)) 




