#create a decorater and use it
def cough_dec(func):
    def wrapper():
        #code before function
        print('#cough')
        func()
        #more code
        print('*cough')
    return wrapper


@cough_dec #its a function, it's  a wrapper
def question():
    print('can you give a discount for your brain')
question()


@cough_dec
def answer():
    print('I have nothing in there')
answer()