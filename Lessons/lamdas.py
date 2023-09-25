#similar to anonymous function
nums=[1,2,3,4,5,6]


num=lambda a,b: a+b


def square(n): #normal function
    return n*n
print(list(map(square,nums)))


lambda n: n*n  #lambda expression

print(list(map(lambda n: n*n,nums)))