#set of key value pairs
ninja_belts={
    'crystal':'red',
    'ryu':'black'
}

ninja_belts['gold']='yellow' #adding key values
print(ninja_belts)
print(ninja_belts['crystal'])
print(list(ninja_belts.keys())) #access the keys in a dictionary
vals=list(ninja_belts.values())
print(vals) #access values in a dictionary
print(vals.count('red'))


# # # ##create a dict use, dict()
# # # person=dict(name='Mary', age=45, status='Married')
# # # print(person)

# # # #Example

# # # def ninja_intro(dictionary):
# # #     for key,val in dictionary.items():
# # #         print(f'I am {key} and i am a {val}belt')

# # # ninja_belts={}

# # # while True:
# # #     ninja_name=input('enter ninja name')
# # #     ninja_belt=input('enter belt color')
# # #     ninja_belts[ninja_name]=ninja_belt


# # #     another=input('add another? (y/n)')
# # #     if another=='y':
# # #         continue
# # #     else:
# # #         break

# # # ninja_intro(ninja_belts)


# # #####Using Sets

# # # def belt_count(dictionary):
# # #     pass
# # #     belts=list(dictionary.values())
# # #     for belt in set(belts):
# # #         num=belts.count(belt)
# # #         print(f'there are {num} {belt} belts')

# # # ninja_belts={}

# # # while True:
# # #     ninja_name=input('enter ninja name')
# # #     ninja_belt=input('enter belt color')
# # #     ninja_belts[ninja_name]=ninja_belt


# # #     another=input('add another? (y/n)')
# # #     if another=='y':
# # #         continue
# # #     else:
# # #         break

# # # belt_count(ninja_belts)

# # # def count(sentence):
# # #     sentence= (sentence.split(' '))
# # #     print(sentence)
# # #     pass
# # # sentence='I am loved,loved, i am'
# # # count(sentence)


# # # dict={'sister':'Mary', 'friend':'Mary', 'fiance':'Benjie'}
# # # number=list(dict.values())
# # # for num in set(number):
# # #     times=number.count(num)
# # #     print(f'{num} appears {times} times, {number}')



# # # ninja_belts={'greet':'hey','emoji':'smile'}

# # # print(list(ninja_belts.values()).count('smile'))

# # my_dict={12:'Mercy', 2: 'Tom', 32:'Masibo'}
# # my_keys=list((my_dict.keys()))
# # my_keys.sort()

# # sorted_dict={k: my_dict[k] for k in my_keys}
# # print(sorted_dict)
# # #dict_keys.sort()
# # #my_dict[12]




# def ninja_intro(dictionary):
#     for key,val in dictionary.items():
#         print(f'i am {key} and i am a {val} belt') 

# ninja_belts={}

# while True:
#     ninja_name=input('enter name')
#     ninja_belt=input('belt color')
#     #ninja_belts[ninja_name]=ninja_belt
#     #or
#     ninja_belts.setdefault(ninja_name,ninja_belt)


#     another=input('add another?(y/n)')
#     if another=='y':
#         continue
#     else:
#         break
# ninja_intro(ninja_belts)


#########Task

# Task 1: Calculate Average Grades

# Write a Python program that takes input for students' names and their respective grades, stores them in a dictionary, and then calculates and displays the average grade for all the students. 

marks_store={}

while True:
    
    name=input('Enter student name')
    grades=int(input('enter student grade'))
    marks_store.setdefault(name,grades)

    another=input('add more students and mrks(y/n)')
    if another=='y':
        continue
    else:
        break


def average_grades(dictionary):
    students_marks=sum(dictionary.values()) #[25,40]
    no_of_students=len(dictionary)
    average_marks=(students_marks//no_of_students)
    print(f'the average grade is {average_marks:.3f}')

average_grades(marks_store) 



