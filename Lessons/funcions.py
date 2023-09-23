def greet(name='mercy',time='morn'):
    print(f'Good {time} {name}, hope you are well')

# name=input('enter name')  
# time=input('enter time')  

greet(name='josh')


#area
def area(radius):
    return( 3.142*radius*radius)

def vol(area,length):
    print(area*length)
radius=int(input('enter radius'))
length=int(input('enter length'))


vol(area(radius),length) #pass a function in another