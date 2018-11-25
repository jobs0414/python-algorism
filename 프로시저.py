# def add_and_display(n1,n2,n3,n4): 

#     result = n1+n2+n3+n4 
#     print(result)


# a= int(input())
# b= int(input())
# c= int(input())
# d= int(input())

# add_and_display(a,b,c,d)


def minimum(va1, va2, va3): 
    mini = va1 
    if  va2 < mini:
        mini = va2 

    if va3 < mini:
        mini = va3
    print("최소값은 {}".format(mini))


minimum(11,12,13)
