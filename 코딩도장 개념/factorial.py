# n! 팩토리얼 값을 구하여라. 

def factorial(n):
    if n ==1: 
        return 1 

    else: 
        return n * factorial(n-1)



print(factorial(5))