grades=['A','B','C', 'F','B','F']

#filter(function,grades)

def remove_fails(grade):
    return grade != 'F'
print(list(filter(remove_fails,grades)))


#use for loop#
filtered_grades=[]

for grade in grades:
    if grade !='F':
        filtered_grades.append(grade)
print(filtered_grades)

#comprehension
print([grade for grade in grades if grade !='F'])