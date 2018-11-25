# def hello(): 
#     print("안녕하세요")
#     hello()

# hello()   무한 재귀 호출 


def hello(count): 

    if count==0: 
        return 

    print("hello",count)
    count -=1
    hello(count)



hello(5)

#아하 재귀호출 
