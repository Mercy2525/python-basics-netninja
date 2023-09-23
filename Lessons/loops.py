# #####FOR LOOP!!!
# friends=['tosh','kama','tabs','jess']

# # for friend in friends: #loops through the whole list
# #     print(friend.title())

# # for friend in friends[0:2]: #loop through a portion(slice)
# #     print(friend)    

# # for friend in friends:
# #     if friend=='tosh':
# #         print(f'{friend} is the OG')
# #         break #breaks and loops through the first condition
# #     else:
# #         print(friend) 
# # 
# # 
# #    

# ##### WHILE LOOP
# age =25
# num =0 

# while num<age: #as long as this is true,it will cycle through the code
#     pass
#     if num==0:
#         num+=1
#         continue #removes the zero, in the loop
#     if num%2==0:
#         print(num)
#     if num>10:
#         break
#     num +=1


# ####Range

# # for n in range(3,10,2): # 1.start 2.stop 3.step
# #         print(n)


burgers=['beef','chicken','veg','supreme','double']

# for n in range(len(burgers)):
#     pass
#     print(n,burgers[n])


for i in range(len(burgers)-1,-1,-1):
    print(i,burgers[i])