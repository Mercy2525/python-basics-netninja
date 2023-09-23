#Numbers
#division returns float

#print(10%3)
#print(type(3.234))

age= 30
#age-=4,,, age +=6,, age/=
age -=6
#print(age)

#Strings

sent= "He's a mad man"
#print(sent[2:-2])
str2='dudes'
combo= sent+ ' '+str2
#print(combo*2)

#print(sent.title())

cheeses='chedar,mozarella,stilton'
split= cheeses.split(',')
#print(len(cheeses))

#Lists
str='Hello, I am lovely'
#print(str.split(','))

fib1=[1,1,2,3,5,8,13]
#print(fib1[0:4])

fib2=[21,34,55]


fib=fib1+fib2
fib.append(89)
fib.append(89)
#fib.pop()
#fib.remove(89)
#print(fib.count(89))
#print(fib.index(89))

del(fib[2])
#print(fib)

char=['me','you','her']
total=[char,fib1,[1,2,3]]
#print(total[0][2])






# #LIST COMPREHENSION

prizes=[5,10,50,100,100]

# # double_prizes=[]

# # for prize in prizes:
# #     double_prizes.append(prize*2)
# # print(double_prizes)

double_prizes=(prize+3 for prize in prizes)
print(double_prizes)



# #1.what we want to appear in each element
# #2.what we loop through

# dbl_prizes=[prize*2 for prize in prizes]
# print(dbl_prizes)




#square numbers(even)
nums=[1,2,3,4,6,7,9]

# square_even_num=[]

# #for loop
# for num in nums:
#     if(num%2)==0:
#         square_even_num.append(num*num)
# print(square_even_num)

# squared_evn_number=[num1*num1 for num1 in nums if(num1%2)==0]
# print(squared_evn_number)



# #or comprehension method

# squared_evn_nums=[num*num for num in nums if(num**2)%2==0]
# print(squared_evn_nums)

